import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_risk_analysis(contract_code, similar_cases):
    context = "\n\n".join([
        f"{case['metadata']['type']}: {case['metadata']['description']}"
        for case in similar_cases
    ])

    prompt = f"""
You are a smart contract security auditor.

Smart Contract:
{contract_code}

Similar Known Vulnerabilities:
{context}

Analyze the risk and provide:
- Risk Score (0-1)
- Detected Patterns
- Explanation
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]