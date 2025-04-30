from decimal import Decimal
from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid


class OrderSchema(SQLModel):
    total: Decimal = Field(max_digits=8, decimal_places=2, nullable=False)
    state: str = Field(max_length=20, nullable=False)

    user_id: uuid.UUID = Field(nullable=False)  # FK


class Order(OrderSchema, table=True):
    __tablename__ = "orders"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    date: datetime = Field(default=datetime.now(), nullable=False)


class OrderProductLink(SQLModel, table=True):
    __tablename__ = "orders_has_products"

    order_id: uuid.UUID = Field(foreign_key="orders.id", primary_key=True)
    product_id: uuid.UUID = Field(primary_key=True)  # FK
    quantity: int = Field(nullable=False)
