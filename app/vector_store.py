from endee import Client

client = Client()

COLLECTION_NAME = "smart_contract_vulnerabilities"

def insert_vector(id, embedding, metadata):
    client.insert(
        collection=COLLECTION_NAME,
        id=id,
        vector=embedding,
        metadata=metadata
    )

def search_similar(embedding, top_k=5):
    return client.search(
        collection=COLLECTION_NAME,
        vector=embedding,
        top_k=top_k
    )