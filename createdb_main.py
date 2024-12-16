#Import db1_utils
from db1_utils import add_documents_to_qdrant_db, add_documents_to_chroma_db, add_documents_to_faiss_db
from db1_utils import create_pinecone_index, add_documents_to_pinecone_index

#Import create_domain_docs
from create_domain_docs import agriculture_food_docs, automotive_transportation_docs, education_academia_docs
from create_domain_docs import environment_sustainability_docs, finance_economics_docs, healthcare_medicine_docs
from create_domain_docs import retail_ecommerce_docs, sports_fitness_docs, technology_innovation_docs, travel_tourism_docs

#Add a logger
import logging
log = logging.getLogger(__name__)

#Write the logs to a file
logging.basicConfig(filename='createdb_main.log', level=logging.INFO)

#Write the initial message to the log file
log.info(f"Starting createdb_main.py")

#Create a function to add documents to all vector databases
def main():
    """
    Main function to add documents to all vector databases.

    This function initializes a Pinecone index and adds documents to it.
    It also adds documents to Qdrant, FAISS, and Chroma vector databases.

    Args:
        None

    Returns:
        None
    """
    # Create a Pinecone index
    pinecone_index = create_pinecone_index()
    log.info(f"Pinecone index created")

    # Add documents to the Pinecone vector database with agriculture_food_docs
    add_documents_to_pinecone_index(pinecone_index, agriculture_food_docs)
    log.info(f"Added {len(agriculture_food_docs)} documents to Pinecone index")

    # Add documents to the Qdrant vector database with automotive_transportation_docs
    add_documents_to_qdrant_db(automotive_transportation_docs)
    log.info(f"Added {len(automotive_transportation_docs)} documents to Qdrant vector database")

    # Add documents to the FAISS vector database with education_academia_docs
    add_documents_to_faiss_db(education_academia_docs)
    log.info(f"Added {len(education_academia_docs)} documents to FAISS vector database")

    # Add documents to the Chroma vector database with environment_sustainability_docs
    add_documents_to_chroma_db(environment_sustainability_docs)
    log.info(f"Added {len(environment_sustainability_docs)} documents to Chroma vector database")

# Run the main function
if __name__ == "__main__":
    log.info(f"Running main function from createdb_main.py")
    main()
