from fastapi import APIRouter

router = APIRouter()

@router.get("/categories")
def get_categories():
    return {"categories": ["Food", "Transport", "Shopping"]}

@router.post("/categories")
def add_category():
    return {"message": "Category added"}