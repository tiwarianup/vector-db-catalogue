import os
import time
from uuid import uuid4

#Use ollama for embeddings model
from langchain_ollama import OllamaEmbeddings

#Langchain imports
from langchain_core.documents import Document

#Import pinecone
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

#Import chroma
from langchain_chroma import Chroma

#Import FAISS
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore

#Import Qdrant
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from dotenv import load_dotenv
load_dotenv()

#Create an OllamaEmbeddings object using nomic-embed-text embedding model
embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

#Add a logger
import logging
log = logging.getLogger(__name__)

#Write the logs to a file
logging.basicConfig(filename='db1_utils.log', level=logging.INFO)

#Write the initial message to the log file
log.info(f"Starting db1_utils.py")

############# Pinecone #############

#Get the Pinecone API key from environment variables
pinecone_api_key = os.environ.get("PINECONE_API_KEY")

#Create a Pinecone client using the API key
pc = Pinecone(api_key=pinecone_api_key)

#Create a function to create a vector database index using Pinecone and Langchain
def create_pinecone_index() -> Pinecone.Index:
    """
    Creates a vector database using Pinecone and Langchain.

    Args:
        None

    Returns:
        index: a Pinecone Index object
    """
    index_name = "domain-pinecone-db-index"

    if index_name not in pc.list_indexes():
        pc.create_index(
            name=index_name,
            dimension=768,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

        # wait for index to be ready
        while not pc.describe_index(index_name).status["ready"]:
            time.sleep(1)

        

    log.info(f"Index {index_name} created")
    return pc.Index(index_name)

#Create a function to add documents to a vector database index using Pinecone and Langchain
def add_documents_to_pinecone_index(index: Pinecone.Index, docs: list[Document]):
    """
    Adds documents to a Pinecone index using Langchain.

    Args:
        index: A Pinecone Index object.
        docs: A list of Document objects.

    Returns:
        None
    """
    vector_store = PineconeVectorStore(index=index, embedding=embeddings)

    # Create a list of unique IDs for the documents
    doc_ids = [str(uuid4()) for _ in range(len(docs))]

    # Add the documents to the vector store
    vector_store.add_documents(documents=docs, ids=doc_ids)
    log.info(f"Added {len(docs)} documents to Pinecone index")

########## Chroma ############

#Create a function to create a vector database using Chroma and Langchain
def add_documents_to_chroma_db(docs: list[Document]):
    """
    Creates a vector database using Chroma and Langchain.

    Args:
        docs: A list of Document objects.

    Returns:
        None
    """
    vector_store = Chroma(
        collection_name="domain_sample",
        embedding_function=embeddings,
        persist_directory="./langchain_chroma_db",  # Where to save data locally, remove if not necessary
    )

    # Create a list of unique IDs for the documents
    doc_ids = [str(uuid4()) for _ in range(len(docs))]

    # Add the documents to the vector store
    vector_store.add_documents(documents=docs, ids=doc_ids)
    log.info(f"Added {len(docs)} documents to Chroma vector database")

########## FAISS ############

#Create a function to create a vector database using FAISS and Langchain
def add_documents_to_faiss_db(docs: list[Document]):
    """
    Creates a vector database using FAISS and Langchain.

    Args:
        docs: A list of Document objects.

    Returns:
        None
    """
    index = faiss.IndexFlatL2(len(embeddings.embed_query("domain-faiss-db-index")))
    log.info(f"Created FAISS index")

    vector_store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={},
    )
    vector_store = FAISS.from_documents(docs, embeddings)    

    # Create a list of unique IDs for the documents 
    doc_ids = [str(uuid4()) for _ in range(len(docs))]

    # Add the documents to the vector store 
    vector_store.add_documents(documents=docs, ids=doc_ids) 
    log.info(f"Added {len(docs)} documents to FAISS vector database")

    # Save the vector store to local storage
    vector_store.save_local("./langchain_faiss_db")
    log.info(f"Saved FAISS index to local:langchain_faiss_db")

########### Qdrant ############

#Create a function to create a vector database using Qdrant and Langchain
def add_documents_to_qdrant_db(docs: list[Document]):
    """
    Creates a vector database using Qdrant and Langchain.

    Args:
        docs: A list of Document objects.

    Returns:
        None
    """    
    client = QdrantClient(path="./langchain_qdrant_db")

    client.create_collection(
        collection_name="domain_sample",
        vectors_config=VectorParams(size=768, distance=Distance.COSINE),
    )

    vector_store = QdrantVectorStore(
        client=client,
        collection_name="domain_sample",
        embedding=embeddings,
    )

    # Create a list of unique IDs for the documents
    doc_ids = [str(uuid4()) for _ in range(len(docs))]

    # Add the documents to the vector store
    vector_store.add_documents(documents=docs, ids=doc_ids) 
    log.info(f"Added {len(docs)} documents to Qdrant vector database")    

