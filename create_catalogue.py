# Import necessary functions to fetch metadata from vector databases
from fetch_db_records import fetch_metadata_from_faiss_db, fetch_metadata_from_pinecone_db
from fetch_db_records import fetch_metadata_from_qdrant_db, fetch_metadata_from_chroma_db

# Import pandas for data manipulation
import pandas as pd

# Fetch metadata from Faiss, Pinecone, Qdrant, and Chroma vector databases
faiss_metadatas = fetch_metadata_from_faiss_db()
pinecone_metadatas = fetch_metadata_from_pinecone_db()
qdrant_metadatas = fetch_metadata_from_qdrant_db()
chroma_metadatas = fetch_metadata_from_chroma_db()

# Convert metadata into pandas DataFrames and add a column to indicate the source vector database
faiss_df = pd.DataFrame(faiss_metadatas)
faiss_df['vector_db_source'] = 'faiss'

pinecone_df = pd.DataFrame(pinecone_metadatas)
pinecone_df['vector_db_source'] = 'pinecone'

qdrant_df = pd.DataFrame(qdrant_metadatas)
qdrant_df['vector_db_source'] = 'qdrant'

chroma_df = pd.DataFrame(chroma_metadatas)
chroma_df['vector_db_source'] = 'chroma'

# Print the first few rows of each DataFrame
print(faiss_df.head())
print(pinecone_df.head())
print(qdrant_df.head())
print(chroma_df.head())

# Concatenate all DataFrames into a single DataFrame
df = pd.concat([faiss_df, pinecone_df, qdrant_df, chroma_df], ignore_index=True)

# Print the first few rows of the concatenated DataFrame
print(df.head())

# Save the concatenated DataFrame to a CSV file
df.to_csv('vectordb_catalogue.csv', index=False)
