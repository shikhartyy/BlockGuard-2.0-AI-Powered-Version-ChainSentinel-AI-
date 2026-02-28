# 🚀 BlockGuard-2.0-AI-Powered-Version-ChainSentinel-AI
### AI-Powered Smart Contract Risk Intelligence using Endee Vector Database

---

## 📌 Project Overview

**ChainSentinel AI** is a Retrieval-Augmented Generation (RAG) based smart contract security assistant that detects and explains potential vulnerabilities in blockchain smart contracts using semantic vector search.

Traditional smart contract scanners rely on static pattern matching and predefined rules. These approaches often fail to capture contextual vulnerabilities or evolving attack patterns.

ChainSentinel AI solves this by:

- Embedding smart contract code into vector space
- Storing known vulnerability reports in Endee (vector database)
- Performing semantic similarity search
- Retrieving relevant vulnerability cases
- Generating contextualized risk analysis using an LLM

This enables intelligent, explainable, and continuously expandable smart contract auditing.

---

## 🎯 Problem Statement

Smart contract vulnerabilities such as:

- Reentrancy
- Integer Overflow / Underflow
- Access Control Misconfiguration
- Front-running
- Gas Optimization Risks

are difficult to detect using static rule-based systems.

Developers need:

- Context-aware security analysis
- Similar historical vulnerability references
- Clear explanations, not just flags
- Scalable and extensible detection

ChainSentinel AI provides an AI-driven solution where vector search is the core retrieval engine.

---

## 🏗️ System Architecture

User Smart Contract  
        ↓  
Embedding Model (Sentence Transformers)  
        ↓  
Endee Vector Database  
        ↓  
Top-K Similar Vulnerability Reports  
        ↓  
LLM (RAG Layer)  
        ↓  
Structured Risk Report  

---

## 🧠 Technical Approach

### 1️⃣ Embedding Layer
- Smart contract code is converted into vector embeddings using Sentence Transformers.
- Known vulnerability reports are embedded and stored in Endee.

### 2️⃣ Vector Storage (Endee)
- Endee is used as the vector database.
- Each vulnerability report is stored with:
  - Unique ID
  - Embedding vector
  - Metadata (type, severity, description)

### 3️⃣ Semantic Retrieval
- When a new contract is submitted:
  - Its embedding is generated.
  - Endee performs cosine similarity search.
  - Top-K relevant vulnerabilities are retrieved.

### 4️⃣ RAG Pipeline
- Retrieved vulnerabilities are injected into the LLM prompt.
- LLM generates:
  - Risk summary
  - Detected patterns
  - Explanation
  - Confidence score

---

## 🧩 How Endee Is Used

Endee serves as the core intelligence retrieval engine of the system.

It is used to:

- Store vulnerability embeddings
- Perform high-performance vector similarity search
- Retrieve contextually similar smart contract vulnerabilities
- Enable scalable and extensible knowledge expansion

Without Endee, the RAG system would not have semantic retrieval capabilities.

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Endee (Vector Database)
- Sentence Transformers
- OpenAI API / Local LLM
- Docker (Optional)

---

## 📂 Project Structure
