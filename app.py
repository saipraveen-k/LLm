from fastapi import FastAPI, Request
from query_parser import extract_info
from rag_engine import get_answer

app = FastAPI()

@app.post("/evaluate_query")
async def evaluate(request: Request):
    body = await request.json()
    user_query = body.get("query")
    extracted = extract_info(user_query)
    decision = get_answer(user_query)
    
    return {
        "query_details": extracted,
        "decision": decision
    }
