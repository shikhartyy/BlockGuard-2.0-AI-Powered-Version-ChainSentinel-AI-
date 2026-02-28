import os
import json
import logging
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from app.embedding import generate_embedding
from app.vector_store import search_similar
from app.rag_pipeline import generate_risk_analysis

# =========================
# Load Environment Variables
# =========================
load_dotenv()

TOP_K = int(os.getenv("TOP_K", 3))

# =========================
# Logging Setup
# =========================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =========================
# FastAPI App
# =========================
app = FastAPI(
    title="BlockGuard 2.0 - AI Smart Contract Risk Analyzer",
    description="RAG-based smart contract vulnerability detection using Endee vector database.",
    version="1.0.0"
)

# =========================
# Request Schema
# =========================
class ContractRequest(BaseModel):
    contract_code: str


# =========================
# Health Check Endpoint
# =========================
@app.get("/")
def root():
    return {"message": "BlockGuard 2.0 API is running."}


# =========================
# Analyze Endpoint
# =========================
@app.post("/analyze")
def analyze_contract(request: ContractRequest):
    try:
        logger.info("Received contract for analysis")

        # Step 1: Generate embedding
        embedding = generate_embedding(request.contract_code)
        logger.info("Embedding generated")

        # Step 2: Retrieve similar vulnerabilities
        similar_cases = search_similar(embedding, top_k=TOP_K)
        logger.info(f"Retrieved {len(similar_cases)} similar cases")

        # Step 3: Generate risk analysis using RAG
        analysis_result = generate_risk_analysis(
            request.contract_code,
            similar_cases
        )
        logger.info("LLM analysis completed")

        return {
            "status": "success",
            "analysis": analysis_result,
            "retrieved_cases": similar_cases
        }

    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }