from fastapi import FastAPI
from app.routers import products


app = FastAPI()
app.include_router(products.router, prefix="/products", tags= ["Products"])

@app.get("/")
def home():
    return {"message": "CloudCart Backend Running"}
