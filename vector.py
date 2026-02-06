from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

pdf_link = "./data/20240716890312078.pdf"
pdfs = [pdf_link]

db_location = "./chroma_langchain_db"

def pdfs_to_sqlite_embeddings(pdf_paths, sqlite_db_path):
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    vector_store = Chroma(
        collection_name="pdf_embeddings",
        persist_directory=sqlite_db_path,
        embedding_function=embeddings
    )

    for pdf_path in pdf_paths:
        loader = PyPDFLoader(pdf_path)
        docs = loader.load_and_split()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(docs)
        vector_store.add_documents(documents=chunks)
        print(f"Added embeddings for {pdf_path}")

    
    print(f"All embeddings stored in SQLite DB at: {sqlite_db_path}")

# Create embeddings if DB doesn’t exist
if not os.path.exists(db_location):
    pdfs_to_sqlite_embeddings(pdfs, db_location)

# Load existing Chroma DB
vector_store = Chroma(
    collection_name="pdf_embeddings",
    persist_directory=db_location,
    embedding_function=OllamaEmbeddings(model="mxbai-embed-large")
)

retriever = vector_store.as_retriever(search_kwargs={"k": 7})
