#Import Faiss vector database
import faiss
from langchain_community.vectorstores import FAISS

#Import Pinecone vector database
import pinecone
from langchain_pinecone import Pinecone
from langchain_pinecone.vectorstores import PineconeVectorStore

#Import Qdrant vector database
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

#Import Chroma vector database
from langchain_chroma import Chroma

#Use ollama for embeddings model
from langchain_ollama import OllamaEmbeddings

#Create an OllamaEmbeddings object using nomic-embed-text embedding model
embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

#Add a logger
import logging
log = logging.getLogger(__name__)

#Write the logs to a file
logging.basicConfig(filename='fetch_db_records.log', level=logging.INFO)

#Write the initial message to the log file
log.info(f"Starting fetch_db_records.py")

#Create a function to fetch all data from Faiss vector database
def fetch_metadata_from_faiss_db() -> list[dict]:
    """
    Retrieve all metadata from a Faiss vector database.

    This function fetches all the metadata from a Faiss vector database
    and returns it as a list of dictionaries.

    Returns:
        metadatas: A list of metadata dictionaries from the index.
    """
    # Load the Faiss vector database from local storage
    faiss_db = FAISS.load_local(
        "langchain_faiss_db", embeddings=embeddings, allow_dangerous_deserialization=True
    )

    # Get all the document IDs from the Faiss index
    all_doc_ids = list(faiss_db.docstore._dict.keys())

    metadatas = []

    # Iterate over each document ID and fetch the metadata
    for doc_id in all_doc_ids:
        document = faiss_db.docstore.search(doc_id)
        if document:
            # Add the metadata to the list
            metadatas.append({"doc_id": doc_id, "metadata": document.metadata})

    return metadatas


#Create a function to fetch all data from Pinecone vector database
def fetch_metadata_from_pinecone_db() -> list[dict]:
    """
    Retrieve all metadata from a Pinecone index.

    This function fetches all the metadata from a Pinecone index
    and returns it as a list of dictionaries.

    Returns:
        metadatas: A list of metadata dictionaries from the index.
    """

    index_name = "domain-pinecone-db-index"
    index = Pinecone.from_existing_index(index_name, embeddings)

    # Get all the document IDs from the index
    doc_ids = list(index._index.list())[0]

    metadatas = []
    # Iterate over each document ID and fetch the metadata
    for doc_id in doc_ids:
        result = index._index.fetch([doc_id])['vectors'][doc_id]

        if result:
            metadata = result["metadata"]
            # Add the metadata to the list
            metadatas.append({"doc_id": doc_id, "metadata": metadata})

    return metadatas

#Create a function to fetch all data from Chroma vector database
def fetch_metadata_from_qdrant_db() -> list[dict]:
    """
    Retrieve all metadata from a Qdrant vector database.

    This function fetches all the metadata from a Qdrant index
    and returns it as a list of dictionaries.

    Returns:
        metadatas: A list of metadata dictionaries from the index.
    """
    # Create a Qdrant client using the path to the database
    client = QdrantClient(path="./langchain_qdrant_db")

    # Set the collection name
    collection_name = "domain_sample"

    # Fetch all the documents from the collection
    response = client.scroll(collection_name=collection_name)

    # Declare a list to store the metadata
    metadatas = []

    # Iterate over each document ID and fetch the metadata
    for resp in response[0]:
        # Convert the response to a dictionary
        result = dict(resp)

        # Get the document ID and metadata
        doc_id = result["id"]
        metadata = result["payload"]["metadata"]

        # Check if the document ID and metadata exist
        if doc_id and metadata:
            # Add the metadata to the list
            metadatas.append({"doc_id": doc_id, "metadata": metadata})

    return metadatas

#Create a function to fetch all data from Chroma vector database
def fetch_metadata_from_chroma_db() -> list[dict]:
    """
    Retrieve all metadata from a Chroma vector database.

    This function fetches all the metadata from a Chroma index
    and returns it as a list of dictionaries.

    Returns:
        metadatas: A list of metadata dictionaries from the index.
    """
    # Specify the collection name
    collection_name = "domain_sample"

    # Initialize the Chroma vector store
    vector_store = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory="./langchain_chroma_db"
    )

    # Retrieve all documents from the collection
    collection_data = vector_store._collection.get()

    # Initialize a list to store metadata
    metadatas = []

    # Iterate over each document ID and fetch the corresponding metadata
    for doc_id, metadata in zip(collection_data['ids'], collection_data['metadatas']):
        if doc_id and metadata:
            metadatas.append({"doc_id": doc_id, "metadata": metadata})

    return metadatas




## ====================================================
#Call the functions for Testing

# print("Fetching data from faiss database")
# print(fetch_metadata_from_faiss_db())   
# print("\n\n")

# print("Fetching data from pinecone database")
# print(fetch_metadata_from_pinecone_db())
# print("\n\n")

# print("Fetching data from Qdrant database")
# print(fetch_metadata_from_qdrant_db())
# print("\n\n")

# print("Fetching data from Chroma database")
# print(fetch_metadata_from_chroma_db())
# print("\n\n")
## ======================================================