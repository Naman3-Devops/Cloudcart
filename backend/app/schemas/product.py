from pydantic import BaseModel


# Pydantic schema
# Used for validating incoming API requests
class Product(BaseModel):

    # Product name
    name: str

    # Product price
    price: float