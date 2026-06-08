from Backend.database import Base

from Backend.auth import get_current_user
from fastapi import APIRouter, Depends
from Backend.auth import get_current_user

router = APIRouter()

# --- Categories Endpoints ---

@router.get("/categories")
def get_categories(current_user=Depends(get_current_user)):
    # In the future, this will fetch default + custom user categories from DB
    return {"categories": ["Food", "Transport", "Bills", "Salary", "Freelance"]}

@router.post("/categories")
def create_category(category_name: str, current_user=Depends(get_current_user)):
    return {"message": f"Category '{category_name}' created successfully"}


# --- Summary Endpoints ---

@router.get("/summary")
def get_monthly_summary(month: str, current_user=Depends(get_current_user)):
    """
    Expects month format: YYYY-MM (e.g., 2026-06)
    """
    # Hardcoded placeholder values for now until DB query logic is built
    total_income = 5000.00
    total_expenses = 3200.00
    net_balance = total_income - total_expenses
    
    return {
        "month": month,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_balance": net_balance
    }
@router.get("/summary")
def summary():
    return {
        "income": 50000,
        "expenses": 25000,
        "savings": 25000
    }
