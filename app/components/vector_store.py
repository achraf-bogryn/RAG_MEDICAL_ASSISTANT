# from langchain_community.vectorstores import FAISS
# import os
# from app.components.embeddings import get_embedding_model

# from app.common.logger import get_logger
# from app.common.custom_exception import CustomException

# from app.config.config import DB_FAISS_PATH

# logger = get_logger(__name__)

# def load_vector_store():
#     try:
#         embedding_model = get_embedding_model()

#         if os.path.exists(DB_FAISS_PATH):
#             logger.info("Loading existing vectorstore...")
#             return FAISS.load_local(
#                 DB_FAISS_PATH,
#                 embedding_model,
#                 allow_dangerous_deserialization=True
#             )
#         else:
#             logger.warning("No vectore store found..")

#     except Exception as e:
#         error_message = CustomException("Failed to load vectorstore" , e)
#         logger.error(str(error_message))

# # Creating new vectorstore function
# def save_vector_store(text_chunks):
#     try:
#         if not text_chunks:
#             raise CustomException("No chunks were found..")
        
#         logger.info("Generating your new vectorstore")

#         embedding_model = get_embedding_model()

#         db = FAISS.from_documents(text_chunks,embedding_model)

#         logger.info("Saving vectorstoree")

#         db.save_local(DB_FAISS_PATH)

#         logger.info("Vectostore saved sucesfulyy...")

#         return db
    
#     except Exception as e:
#         error_message = CustomException("Failed to craete new vectorstore " , e)
#         logger.error(str(error_message))
    

from langchain_community.vectorstores import FAISS
import os
from functools import lru_cache

from app.components.embeddings import get_embedding_model
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import DB_FAISS_PATH

logger = get_logger(__name__)

@lru_cache(maxsize=1)
def _cached_embeddings():
    """Load embeddings once per process (huge speed win)."""
    return get_embedding_model()

def load_vector_store():
    """Load existing FAISS vector store from disk."""
    try:
        if not os.path.exists(DB_FAISS_PATH):
            raise CustomException(f"No vector store found at: {DB_FAISS_PATH}")

        logger.info("Loading existing vectorstore...")
        embedding_model = _cached_embeddings()

        return FAISS.load_local(
            DB_FAISS_PATH,
            embedding_model,
            allow_dangerous_deserialization=True
        )

    except Exception as e:
        error_message = CustomException("Failed to load vectorstore", e)
        logger.error(str(error_message))
        return None

def save_vector_store(text_chunks):
    """Create + save FAISS vector store from chunks."""
    try:
        if not text_chunks:
            raise CustomException("No chunks were found..")

        logger.info("Generating your new vectorstore...")
        embedding_model = _cached_embeddings()

        db = FAISS.from_documents(text_chunks, embedding_model)

        logger.info("Saving vectorstore...")
        os.makedirs(DB_FAISS_PATH, exist_ok=True)  # ensure folder exists
        db.save_local(DB_FAISS_PATH)

        logger.info("Vectorstore saved successfully.")
        return db

    except Exception as e:
        error_message = CustomException("Failed to create new vectorstore", e)
        logger.error(str(error_message))
        return None

def load_or_build_vector_store(text_chunks=None):
    """
    If FAISS exists -> load it.
    If missing -> build from provided chunks and save.
    """
    if os.path.exists(DB_FAISS_PATH):
        return load_vector_store()

    if text_chunks is None:
        raise CustomException(
            "Vectorstore missing and no chunks provided to build it."
        )

    return save_vector_store(text_chunks)