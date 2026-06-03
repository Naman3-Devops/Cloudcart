from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Database dependency
from app.database import get_db

# SQLAlchemy database model
from app.models.product import Product

# Pydantic schema for request validation
from app.schemas.product import Product as ProductSchema

# Create router object
router = APIRouter()

# Temporary in-memory storage
# Will be removed once all CRUD uses PostgreSQL
products = []


# Get products from temporary list
@router.get("/")
def get_products(limit: int = 10):

    return products[:limit]


# Get all products from PostgreSQL
@router.get("/db")
def get_products_from_db(db: Session = Depends(get_db)):

    products = db.query(Product).all()

    return products


# Get one product by index from temporary list
@router.get("/{product_id}")
def get_product(product_id: int):

    if product_id < len(products):

        return products[product_id]

    return {
        "error": "Product not found"
    }


# Delete product from temporary list
@router.delete("/{product_id}")
def delete_product(product_id: int):

    if product_id < len(products):

        deleted_product = products.pop(product_id)

        return {
            "message": "Product deleted",
            "deleted_product": deleted_product
        }

    return {
        "error": "Product not found"
    }


# Update product in temporary list
@router.put("/{product_id}")
def update_product(
    product_id: int,
    product: ProductSchema
):

    if product_id < len(products):

        products[product_id] = product.model_dump()

        return {
            "message": "Product updated",
            "product": products[product_id]
        }

    return {
        "error": "Product not found"
    }


# Create product in temporary list
@router.post("/")
def create_product(product: ProductSchema, db: Session = Depends(get_db)):

    #Create SQLAlchemy product object
    new_product = Product(
        name=product.name,
        price=product.price,
    )

    #add product to session
    db.add(new_product)

    #save to PostgreSQL
    db.commit()

    #Refresh object to get generated ID
    db.refresh(new_product)


    return {
        "message": "Product created",
        "product": {
            "id": new_product.id,
            "name": new_product.name,
            "price": new_product.price,
            
        }
    }