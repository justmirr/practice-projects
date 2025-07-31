# a simple FastAPI app to revise the basic concepts

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# pydantic model
class Employee(BaseModel):
    id: int
    name: str
    role: str
    salary: int

EMPLOYEES: List[Employee] = [
    Employee(id=1, name="mir", role="dev", salary=12000)
]

# FastAPI routes
@app.get("/")
def home():
    return "hi, this is a simple employee app"

@app.get("/employees", response_model=List[Employee])
def get_employees():
    return EMPLOYEES

@app.post("/employees", response_model=Employee)
def add_employee(emp: Employee):
    EMPLOYEES.append(emp)
    return emp

@app.get("/search/{id}")
def search_employee(id: int):
    return [emp for emp in EMPLOYEES if emp.id == id]

@app.delete("/delete/{id}")
def delete_employee(id: int):
    for emp in EMPLOYEES:
        if emp.id == id:
            EMPLOYEES.remove(emp)