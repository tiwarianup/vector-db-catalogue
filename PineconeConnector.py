from pinecone import Pinecone, ServerlessSpec
import json

class PineconeDatabaseConnector:
    def __init__(self, api_key, environment, index_name):
        """Initialize connector with Pinecone connection parameters."""
        self.api_key : str = (
            self.service_connection.connectionOptions.__root__.get(api_key)
        )
        self.environment : str = (
            self.service_connection.connectionOptions.__root__.get(environment)
        )

        self.index_name : str = (
            self.service_connection.connectionOptions.__root__.get(index_name)
        )
        
        self.index = None

    def connect(self):
        """Establish connection to the Pinecone index."""
        try:
            # Initialize Pinecone
            pc = Pinecone(
                api_key=self.api_key
            )

            # Create a new index
            if self.index_name not in pc.list_indexes().names():
                pc.create_index(
                    name=self.index_name,
                    dimension=768,
                    metric='cosine',
                    spec=ServerlessSpec(
                        cloud='aws',
                        region='us-east-1"'
                    )
                )
            
            # print(pc.describe_index(self.index_name))

            # Connect to an existing index
            self.index = pc.Index(self.index_name)

            print(f"Connected to Pinecone index '{self.index_name}' successfully.")
        except Exception as e:
            print(f"Error connecting to Pinecone: {e}")
            self.index = None

    def fetch_metadata(self):
        """
        Fetches the metadata from the Pinecone index. 
        Customize this method based on your specific metadata needs.
        """
        if not self.index:
            print("No active index connection.")
            return None

        try:
            # Get all the document IDs from the index
            doc_ids = list(self.index.list())[0]
            metadatas = []

            # Iterate over each document ID and fetch the metadata
            for doc_id in doc_ids:
                result = self.index.fetch([doc_id])['vectors'][doc_id]

                if result:
                    metadata = result["metadata"]
                    # Add the metadata to the list
                    metadatas.append({"doc_id": doc_id, "metadata": metadata})

            return json.dumps(metadatas)
        except Exception as e:
            print(f"Error fetching metadata: {e}")
            return None

    def close(self):
        """Pinecone connections are typically stateless, so no close operation is required."""
        print("Pinecone connection is stateless; nothing to close.")

# # Example usage
# if __name__ == "__main__":
#     connector = PineconeDatabaseConnector(
#         api_key="pcsk_3tPPDr_KYj5t1P1CM6wgQeoFzj9bgGAvmRz6rkGvEoe93E2HoACMHy2NGaeYsD1NJXcwYS",
#         environment="us-east-1",  # e.g. "us-west1-gcp"
#         index_name="domain-pinecone-db-index"
#     )
#     connector.connect()
#     metadata = connector.fetch_metadata()
#     print(metadata)