from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(override=False)

# Get DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Print for debugging
print("DATABASE_URL =", DATABASE_URL)

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base model class
Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
    
