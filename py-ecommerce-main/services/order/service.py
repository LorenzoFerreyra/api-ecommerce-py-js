from uuid import UUID
from sqlmodel import Session, select
from .models import Order, OrderProductLink, OrderSchema
import requests

USER_SERVICE_URL = "http://user:8003"
PRODUCT_SERVICE_URL = "http://product:8001"


class OrderService:
    def __init__(self, session: Session):
        self.session = session

    def get_one(self, order_id: UUID) -> Order | None:
        order = self.session.get(Order, order_id)
        products = self.session.exec(
            select(OrderProductLink).where(OrderProductLink.order_id == order_id)
        ).all()
        if not order:
            return None
        return {"order": order, "products": products}

    def get_all(self, user_id: UUID) -> list[Order]:
        statement = select(Order).where(Order.user_id == user_id)
        return self.session.exec(statement).all()

    def create(self, order: OrderSchema, products: dict[UUID, int]) -> Order:
        user_id = order.user_id
        response = requests.get(f"{USER_SERVICE_URL}/{user_id}")
        if response.status_code != 200:
            raise ValueError("User not found")
        order = Order(total=order.total, state=order.state, user_id=order.user_id)
        try:
            self._valid_products(products)
        except ValueError as e:
            raise e
        self.session.add(order)
        self.session.commit()
        try:
            self.set_products(order.id, products)
        except ValueError as e:
            self.session.delete(order)
            self.session.commit()
            raise e
        self.session.refresh(order)
        return order

    def set_products(self, order_id: UUID, products: dict[UUID, int]):
        for key, value in products.items():
            product_id = key
            quantity = value
            self.session.add(
                OrderProductLink(
                    order_id=order_id, product_id=product_id, quantity=quantity
                )
            )
            # update stock
            requests.patch(
                f"{PRODUCT_SERVICE_URL}/stock",
                json={"product_id": str(product_id), "stock": -quantity},
            )
        self.session.commit()
        return True

    def _valid_products(self, products: dict[UUID, int]):
        for key, value in products.items():
            product_id = key
            quantity = value
            response = requests.get(f"{PRODUCT_SERVICE_URL}/{product_id}")
            if response.status_code != 200:
                raise ValueError(f"Product not found, id: {product_id}")
            if response.json()["stock"] < quantity:
                raise ValueError(f"Not enough stock for this product {product_id}")
