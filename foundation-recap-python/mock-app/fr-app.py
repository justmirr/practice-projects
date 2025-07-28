# a simple FastAPI app that simulates receiving a natural language question, generates a fake SQL query (mocked), and returns a summary - practice for GenAI solutioning

import uuid
import os
import asyncio
import logging

from datetime import datetime
from dataclasses import dataclass

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
logging.basicConfig(level=logging.INFO)

# utility - logging
def get_log_path() -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    return os.path.join(log_dir, f"{today}.log")

def log_message(message: str):
    with open(get_log_path(), "a") as f:
        f.write(message + "\n")

# tool input using dataclass
@dataclass
class ToolInput:
    question: str
    user_id: str

# API input using pydantic
class QueryRequest(BaseModel):
    question: str
    user_id: str

class QueryResponse(BaseModel):
    id: str
    sql: str
    summary: str

# mock function using typing

def generate_mock_sql(tool_input: ToolInput) -> str:
    return f"SELECT * FROM employees WHERE department == 'IT' >> based on {tool_input.question}"

async def generate_summary(sql: str) -> str:
    await asyncio.sleep(1)
    return f"summary: executing the query will return employee data"

# API route
@app.post("/generate", response_model=QueryResponse)
async def handle_query(req: QueryRequest):
    request_id = str(uuid.uuid4())
    tool_input = ToolInput(question=req.question, user_id=req.user_id)

    log_message(f"[{datetime.now()}] request id: {request_id}, question: {tool_input.question}")

    sql = generate_mock_sql(tool_input)
    summary = await generate_summary(sql)

    return QueryResponse(
        id=request_id,
        sql=sql,
        summary=summary
    )