from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI()

class Expense(BaseModel):
    id:int = 0
    title: str
    amount: float
    category: str
    date: date

expenses: List[Expense] = []
current_id = 1

@app.post("/expenses")
def create_expense(expense: Expense):
    global current_id
    expense.id = current_id
    current_id += 1
    expenses.append(expense)
    return expense

@app.get("/expenses")
def get_expenses():
    return expenses

@app.get("/expenses/filter")
def filter_expenses(category: str):
    filtered = [e for e in expenses if e.category == category]
    return filtered

@app.get("/expenses/total")
def get_total():
    total = sum(e.amount for e in expenses)
    return {"total": total}

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    global expenses
    for e in expenses:
        if e.id == expense_id:
            expenses.remove(e)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Expense not found")