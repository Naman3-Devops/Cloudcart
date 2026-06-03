from pydantic import BaseModel


# Base schema
class ProductBase(BaseModel):
    name: str
    price: float


# Used when creating a product
class ProductCreate(ProductBase):
    pass


# Used when returning product data
class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
