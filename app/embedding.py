from sentence_transformers import SentenceTransformer
import os

MODEL_NAME = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")

model = SentenceTransformer(MODEL_NAME)

def generate_embedding(text: str):
    return model.encode(text).tolist()