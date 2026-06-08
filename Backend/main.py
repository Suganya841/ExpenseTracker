from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# Correct absolute imports using the 'Backend.' prefix for Render
from Backend.database import SessionLocal, engine, Base
from Backend.auth import verify_password, create_access_token
from Backend.models import User 
from Backend.expense import router as expense_router 
from Backend.summary import router as summary_router

# Automatically create database tables if they don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")

# Enable CORS so your Streamlit frontend can communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permits requests from any origin (like localhost:8501)
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE
    allow_headers=["*"],
)

# Database Dependency Injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Include Routers
app.include_router(expense_router)
app.include_router(summary_router)

@app.get("/")
def home():
    return {"message": "Expense Tracker API is running successfully!"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # 1. Fetch user from the database
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid Credentials"
        )

    # 2. Verify incoming plain text password against the database hashed password
    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid Credentials"
        )

    # 3. Generate JWT access token
    token = create_access_token(data={"sub": user.username})
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.post("/register")
def register(): 
    # Placeholder - Add your user signup / registration logic here later
    return {"message": "User registration endpoint"}
