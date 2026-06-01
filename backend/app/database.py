from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL connection string
# Format:
# postgresql://username:password@host:port/database_name
DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/cloudcart"

# Creates the connection engine that talks to PostgreSQL
engine = create_engine(DATABASE_URL)

# Creates database sessions
# A session is a temporary conversation between FastAPI and PostgreSQL
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Parent class for all database models
Base = declarative_base()


# Dependency used by FastAPI
# Creates a session for every request
# Closes it automatically when request finishes
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
    
