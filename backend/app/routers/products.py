from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Database dependency
from app.database import get_db

# SQLAlchemy database model
from app.models.product import Product

# Pydantic schema for request validation
from app.schemas.product import(ProductCreate, ProductResponse)

# Create router object
router = APIRouter()

# Temporary in-memory storage
# Will be removed once all CRUD uses PostgreSQL



# Get products from temporary list
@router.get("/", response_model=list[ProductResponse])
def get_products(limit: int = 10, db: Session =  Depends(get_db)):

    products = db.query(Product).limit(limit).all()  

    return products


# Get all products from PostgreSQL
@router.get("/db")
def get_products_from_db(db: Session = Depends(get_db)):

    products = db.query(Product).all()

    return products


# Get one product by index from temporary list
@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="product not found"
        )

    return product

# Delete product from temporary list
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="product not found"
        )
    
    db.delete(product)
    db.commit()

    return{
        "message": "product deleted successfully"
    }


# Update product in temporary list
@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    updated_product: ProductCreate,
    db: Session =  Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:

        raise HTTPException(
            status_code=404,
            detail="product not found"
        )
    

    
    #Update fields
    product.name = updated_product.name
    product.price = updated_product.price

    #save changes
    db.commit()

    #Reload updated data
    db.refresh(product)

    return product

# Create product in temporary list
@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):

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


    return  new_product
    