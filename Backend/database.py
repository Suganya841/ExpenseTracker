import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Grab the URL from Render's environment variables.
# If it doesn't exist, fall back to your local machine's database.
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:Admin123@localhost:5432/expense_db"
)

# 2. Render database strings sometimes start with "postgres://", 
# but modern SQLAlchemy strictly requires "postgresql://". This safe-check fixes that.
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
