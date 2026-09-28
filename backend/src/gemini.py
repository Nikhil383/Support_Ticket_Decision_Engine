from google import genai

from .config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def generate_response(
    customer_message,
    decision,
    documents,
):

    evidence = "\n\n".join(
        f"Source: {metadata.get('source', 'unknown')}\n"
        f"{document}"
        for document, metadata
        in documents
    )

    prompt = f"""
You are a customer support response assistant.

Customer message:
{customer_message}

Structured decision:
{decision}

Knowledge-base evidence:
{evidence}

Rules:
- Use supplied evidence.
- Do not invent company policies.
- Do not claim refunds, cancellations, fixes,
  or other actions are completed unless evidence confirms them.
- If evidence is insufficient, say so.
- Keep the response concise and professional.
- Do not mention Laya, RAG, Gemini, or internal routing.

Write only the customer-facing response.
"""

    result = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    return result.text.strip()