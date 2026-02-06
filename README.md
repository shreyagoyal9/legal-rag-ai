# Legal RAG AI

A Retrieval-Augmented Generation (RAG) system for legal case analysis that retrieves relevant laws from PDF documents and generates structured legal reasoning using Large Language Models (LLMs).

This project demonstrates the use of LangChain, ChromaDB, and Ollama to build an end-to-end legal document question-answering pipeline.

---

##  Project Overview

Legal documents are lengthy and complex, making it difficult to quickly identify relevant laws for a given case.  
This project solves that problem by:

- Converting legal PDFs into vector embeddings
- Storing them in a persistent vector database
- Retrieving the most relevant legal sections for a user-provided case
- Generating legal reasoning using a locally hosted LLM

The system behaves like a legal assistant that helps analyze cases based on existing legal documents.



##  System Architecture

1. **PDF Loader**
   - Loads legal documents using `PyPDFLoader`

2. **Text Splitting**
   - Splits documents into overlapping chunks using `RecursiveCharacterTextSplitter`

3. **Embedding Generation**
   - Generates embeddings using Ollama (`mxbai-embed-large`)

4. **Vector Store**
   - Stores embeddings in ChromaDB (SQLite-backed)

5. **Retriever**
   - Retrieves top-k relevant chunks based on semantic similarity

6. **LLM Reasoning**
   - Uses Ollama (`llama3.2`) to generate legal explanations based on retrieved laws

---

##  Project Structure

legal-rag-ai/
│
├── main.py # Main application logic
├── vector.py # PDF embedding and ChromaDB retriever
├── pyproject.toml # Project metadata and dependencies
├── uv.lock # Dependency lock file
├── README.md # Project documentation
├── .gitignore # Ignored files and folders
│
└── data/ # Legal PDF documents (ignored in Git)




##  Tech Stack

- **Python 3.13**
- **LangChain**
- **ChromaDB**
- **Ollama**
- **PyPDF**
- **UV (dependency manager)**

---

##  Setup Instructions

### 1. Clone the repository
bash
git clone https://github.com/shreyagoyal9/legal-rag-ai.git
cd legal-rag-ai

2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install uv
uv sync

# Ollama Setup (Required)

Install Ollama from:

https://ollama.com/download


Pull required models:

ollama pull llama3.2
ollama pull mxbai-embed-large


Ensure Ollama is running:

ollama list

# Running the Application

Add your legal PDF to the data/ folder and update the path in vector.py.

Run:

python main.py


Example input:

A person broke into a house at night and stole gold jewellery worth ₹5 lakhs.


The system will:

Retrieve relevant laws from the document

Generate a legal explanation and applicable articles

# Use Case

Legal document analysis

Case-based law retrieval

Academic demonstrations of RAG systems

AI-assisted legal research (educational purpose)

# Notes

The data/ folder and chroma_langchain_db/ are excluded from version control

All models run locally using Ollama (no cloud dependency)

This project is intended for educational and academic use

# Author

Shreya Goyal
Computer Science Student
GitHub: https://github.com/shreyagoyal9

# License

This project is for academic and learning purposes.




### What you should do now
1. Open `README.md` in VS Code  
2. Replace everything with the content above  
3. Save the file  
4. Commit it:

```bash
git add README.md
git commit -m "Add detailed project README"
git push
