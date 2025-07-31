# dataclass helps you define models without verbose boilerplate, use case - define input types for tools cleanly

from dataclasses import dataclass

@dataclass
class ToolInput:
    query: str
    user_id: int

inp = ToolInput("show me all employees", 101)
print(f"request: {inp.query}, by: {inp.user_id}")