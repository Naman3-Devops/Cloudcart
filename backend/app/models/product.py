from sqlalchemy import Column, Integer, String, Float

from app.database import Base


# SQLAlchemy model
# Represents the products table in PostgreSQL
class Product(Base):

    # PostgreSQL table name
    __tablename__ = "products"

    # Primary key column
    id = Column(Integer, primary_key=True, index=True)

    # Product name
    name = Column(String)

    # Product price
    price = Column(Float)
    