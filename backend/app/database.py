from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load environment variables from .env file
# Example:
# DATABASE_URL=postgresql://postgres:password@localhost:5432/cloudcart
load_dotenv(override=False)

# Read DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create SQLAlchemy engine only if DATABASE_URL exists
#
# Why?
# ----------
# Locally:
#   DATABASE_URL comes from .env file
#
# Docker:
#   DATABASE_URL comes from docker-compose.yml
#
# GitHub Actions:
#   DATABASE_URL may not exist
#
# Without this check, create_engine(None)
# would crash the application and CI pipeline.
if DATABASE_URL:
    engine = create_engine(DATABASE_URL)
else:
    engine = None

# Create database sessions
# A session is a temporary conversation between FastAPI and PostgreSQL
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class inherited by all SQLAlchemy models
#
# Example:
# class Product(Base):
#     ...
Base = declarative_base()


# FastAPI Dependency
#
# Creates a database session for every request
#
# Request starts
#      ↓
# Session opens
#      ↓
# Database query runs
#      ↓
# Session closes automatically
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
    
