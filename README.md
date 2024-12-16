# VectorDB cataloging tool
An experiment to connect various vector databases for metadata discovery and vectordb data source retreival.
An attempt to create a vectordb catalogue

## Selected VectorDBs to work with
- Chroma
- BagelDb
- DuckDb
- Faiss
- LanceDb
- Pinecone
- Weaviate
- Qdrant

### Env1 - vectordb contains pinecone, faiss, chromadb, qdrant
### Env2 - vectordb2 contains duckdb, lancedb
### Env3 - vectordb3 contains weaviate, betabageldb

Steps:
1. Install the necessary packages mentioned in the readme file.
2. Run db1_utils.py to create vectordbs - update indexes and connections as necessary. (To be improved)
3. Run create_catalogue.py to fetch metadata from various vectordbs.
4. Run query_catalogue.py to seach and discover query_catalogue bases on a keyword.
