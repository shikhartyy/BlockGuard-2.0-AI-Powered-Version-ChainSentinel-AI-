import json
from app.embedding import generate_embedding
from app.vector_store import insert_vector

with open("data/vulnerability_reports.json") as f:
    data = json.load(f)

for item in data:
    text = item["description"] + " " + item["example_code"]
    embedding = generate_embedding(text)
    
    insert_vector(
        id=item["id"],
        embedding=embedding,
        metadata=item
    )

print("Data ingestion complete.")