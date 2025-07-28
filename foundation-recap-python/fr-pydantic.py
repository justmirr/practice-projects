# used in LangChain, FastAPI, and agent inputs/outputs, ensures inputs match expected formats, use case - standardize tool inputs, API request schemas

from pydantic import BaseModel

class QueryInput(BaseModel):
    question: str
    connection: str

payload = QueryInput(question="how many projects", connection="mysql")
print(payload.model_dump())