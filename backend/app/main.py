from fastapi import FastAPI

# Database imports
from app.database import Base, engine

# Import model so SQLAlchemy can detect it
from app.models.product import Product

# Import product routes
from app.routers import products

# Create all tables if they don't exist
# Automatically creates tables if they don't exist
#
# Good for learning projects
#
# In production environments, Alembic migrations
# should be used instead of create_all()
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI()


# Home route
@app.get("/")
def home():

    return {
        "message": "Welcome to CloudCart API"
    }


# Register product routes
app.include_router(
    products.router,
    prefix="/products",
    tags=["Products"]
)