from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from Backend.database import SessionLocal, engine, Base
from Backend.auth import (
    verify_password,
    create_access_token,
    hash_password
)
from Backend.models import User

from Backend.expense import router as expense_router
from Backend.summary import router as summary_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Include Routers
app.include_router(expense_router)
app.include_router(summary_router)

# Home Route
@app.get("/")
def home():
    return {
        "message": "Expense Tracker API is running successfully!"
    }

# Register User
@app.post("/register")
def register(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(User)
        .filter(User.username == form_data.username)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )

    new_user = User(
        username=form_data.username,
        password=hash_password(form_data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully! You can login now."
    }

# Login User
@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.username == form_data.username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Credentials"
        )

    if not verify_password(
        form_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Credentials"
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
