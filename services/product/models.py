from decimal import Decimal
from pydantic import HttpUrl
from sqlmodel import SQLModel, Field
from typing import Optional
import uuid


class ProductSchema(SQLModel):
    name: str = Field(max_length=100, nullable=False)
    description: str = Field(max_length=255, nullable=False)
    img: HttpUrl = Field(nullable=False)
    size: Optional[str] = Field(default=None, max_length=20)
    price: Decimal = Field(max_digits=8, decimal_places=2, nullable=False)
    stock: Optional[int] = Field(default=0)

    category_id: Optional[uuid.UUID] = Field(default=None)  # FK


class Product(ProductSchema, table=True):
    __tablename__ = "products"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    img: str = Field(max_length=255, nullable=False)
