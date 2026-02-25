# RAG Medical Assistant

## Project Overview
RAG Medical Assistant is a Retrieval-Augmented Generation (RAG) based chatbot designed to answer medical questions. It uses a combination of vector stores, language models, and custom prompts to provide concise and accurate responses to user queries.

---

## Project Structure
The project is organized as follows:

```
RAG_assistante/
├── requirements.txt          # List of dependencies
├── setup.py                  # Project setup file
├── app/                      # Main application directory
│   ├── __init__.py           # Marks the directory as a Python package
│   ├── application.py        # Flask application entry point
│   ├── common/               # Common utilities
│   │   ├── __init__.py
│   │   ├── custom_exception.py  # Custom exception handling
│   │   └── logger.py         # Logging setup
│   ├── components/           # Core components of the application
│   │   ├── __init__.py
│   │   ├── data_loader.py    # Handles PDF loading and processing
│   │   ├── embeddings.py     # Embedding model loader
│   │   ├── llm.py            # Language model loader
│   │   ├── pdf_loader.py     # PDF file loader and text splitter
│   │   ├── retriever.py      # Retrieval-based QA chain setup
│   │   └── vector_store.py   # Vector store management
│   ├── config/               # Configuration files
│   │   ├── __init__.py
│   │   └── config.py         # Configuration variables
│   └── templates/            # HTML templates for the Flask app
│       └── index.html        # Main UI template
├── data/                     # Directory for storing data files
└── RAG_Medcal_Chatbot.egg-info/  # Metadata for the Python package
```

---

## Key Components

### 1. **Flask Application**
- **File**: `app/application.py`
- **Description**: The entry point for the Flask web application. It handles user interactions, manages sessions, and integrates the QA chain for generating responses.

### 2. **Common Utilities**
- **Logger** (`app/common/logger.py`): Provides a centralized logging mechanism.
- **CustomException** (`app/common/custom_exception.py`): Handles custom exceptions with detailed error messages.

### 3. **Core Components**
- **Data Loader** (`app/components/data_loader.py`): Processes PDF files and stores them in the vector store.
- **Embeddings** (`app/components/embeddings.py`): Loads the HuggingFace embedding model.
- **LLM Loader** (`app/components/llm.py`): Loads the language model using Groq.
- **PDF Loader** (`app/components/pdf_loader.py`): Reads PDF files and splits them into text chunks.
- **Retriever** (`app/components/retriever.py`): Sets up the QA chain using a retriever and custom prompts.
- **Vector Store** (`app/components/vector_store.py`): Manages the FAISS-based vector store for document retrieval.

### 4. **Configuration**
- **File**: `app/config/config.py`
- **Description**: Contains configuration variables such as HuggingFace model ID, database paths, and chunking parameters.

### 5. **Templates**
- **File**: `app/templates/index.html`
- **Description**: Provides the user interface for interacting with the chatbot.

---

## How It Works
1. **User Interaction**:
   - Users interact with the chatbot through the Flask web interface.
   - User queries are sent to the backend for processing.

2. **Data Retrieval**:
   - The vector store retrieves relevant context based on the user query.

3. **Response Generation**:
   - The language model generates a response using the retrieved context and a custom prompt.

4. **Response Display**:
   - The generated response is displayed to the user in the web interface.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/achraf-bogryn/RAG_MEDICAL_ASSISTANT.git
   ```

2. Navigate to the project directory:
   ```bash
   cd RAG_MEDICAL_ASSISTANT
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the Flask application:
   ```bash
   python app/application.py
   ```

---

## Usage
- Open your browser and navigate to `http://127.0.0.1:5000`.
- Ask medical questions and receive concise answers.

---

## Future Improvements
- Add support for more file formats (e.g., Word documents).
- Enhance the user interface with additional features.
- Integrate more advanced language models for better responses.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author
**Achraf Bogryn**

For any inquiries, feel free to contact the author.
