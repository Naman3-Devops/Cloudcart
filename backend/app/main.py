from fastapi import FastAPI

# Import product routes
from app.routers import products

# Create FastAPI application
app = FastAPI()


# Home route
@app.get("/")
def home():

    return {
        "message": "Welcome to CloudCart API"
    }


# Register product routes
# All routes inside products.py will start with /products
app.include_router(
    products.router,
    prefix="/products",
    tags=["Products"]
)
