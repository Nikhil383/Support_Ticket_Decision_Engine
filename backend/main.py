from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from src.laya_engine import DecisionEngine
from src.rag import KnowledgeBase
from src.gemini import generate_response


app = FastAPI(
    title="Laya Gemini RAG API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


decision_engine = DecisionEngine()
knowledge_base = KnowledgeBase()


class AnalyzeRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=3,
        max_length=10000,
    )


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/analyze")
def analyze(request: AnalyzeRequest):

    # 1. Structured decision
    decision = decision_engine.analyze(
        request.message
    )

    # 2. Retrieve knowledge
    documents = knowledge_base.search(
        request.message,
        top_k=3,
    )

    # 3. Generate grounded response
    response = generate_response(
        customer_message=request.message,
        decision=decision,
        documents=documents,
    )

    return {
        "decision": decision,
        "documents": [
            {
                "content": document,
                "metadata": metadata,
            }
            for document, metadata in documents
        ],
        "response": response,
    }