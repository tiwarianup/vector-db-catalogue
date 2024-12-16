import pandas as pd


def query_catalogue(query):
    df = pd.read_csv('./vectordb_catalogue.csv')

    return df[df['metadata'].str.contains(query) | df['vector_db_source'].str.contains(query) | df['doc_id'].str.contains(query)]


if __name__ == '__main__':
    query = input("Enter a query: ")
    print(query_catalogue(query))