from fastapi import APIRouter, Depends
from Backend.auth import get_current_user # Assuming auth.py provides this

router = APIRouter()

# Add a new expense (e.g., specific to an 'Off-Door' category)
@router.post("/appends/off-door") # Adjusted path to lowercase 'off-door' for consistency
def add_off_door_expense(current_user=Depends(get_current_user)):
    return {"message": "Off-Door expense added"}

# This function might be for a general 'add expense' if not categories
# Example: Adding a new expense of a general type. This could be /appends or /expenses
# For clarity, let's make a general purpose add expense on /expenses
@router.post("/expenses")
def add_general_expense(current_user=Depends(get_current_user)):
    return {"message": "General expense added"}

# Get all expenses
@router.get("/expenses")
def get_expenses(current_user=Depends(get_current_user)):
    return {"message": "List of all expenses"}

# Update a specific expense by ID
# Using PUT for updates is standard REST practice
@router.put("/expenses/{id}")
def update_expense(id: int, current_user=Depends(get_current_user)):
    return {"message": f"Expense {id} updated"}

# Delete a specific expense by ID
@router.delete("/expenses/{id}") # This should correctly delete an expense by ID
def delete_expense(id: int, current_user=Depends(get_current_user)):
    return {"message": f"Expense {id} deleted"}

@router.post("/expenses")
def add_general_expense(current_user=Depends(get_current_user)):
    return {"message": "General expense added"}

@router.get("/summary")
def get_summary(month: int):
    return {
        "total_income": 50000,
        "total_expense": 25000,
        "savings": 25000
    }


