from sqlmodel import Session, select
from .models import Product, ProductSchema
from uuid import UUID
import requests

CATEGORY_SERVICE_URL = "http://category:8002"


class ProductService:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Product]:
        return self.session.exec(select(Product)).all()

    def get_one(self, product_id: UUID) -> Product | None:
        return self.session.get(Product, product_id)

    def get_by_category(self, category_id: UUID) -> list[Product]:
        return self.session.exec(
            select(Product).where(Product.category_id == category_id)
        ).all()

    def create(self, product_data: ProductSchema) -> Product:
        if product_data.category_id:
            if not self._validate_category(product_data.category_id):
                raise ValueError("Invalid category")
        product = Product(
            name=product_data.name,
            description=product_data.description,
            img=str(product_data.img),
            size=product_data.size,
            price=product_data.price,
            category_id=product_data.category_id,
            stock=product_data.stock,
        )
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def update_stock(self, product_id: UUID, stock: int) -> Product:
        product = self.get_one(product_id)
        if not product:
            raise ValueError("Product not found")
        product.stock += stock
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def update_category(self, product_id: UUID, category_id: UUID) -> Product:
        product = self.get_one(product_id)
        if not product:
            raise ValueError("Product not found")
        if not self._validate_category(category_id):
            raise ValueError("Invalid category")
        product.category_id = category_id
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def remove_category(self, category_id: UUID):
        statement = select(Product).where(Product.category_id == category_id)
        products = self.session.exec(statement).all()
        for product in products:
            product.category_id = None
        self.session.commit()

    def _validate_category(self, category_id: UUID) -> bool:
        response = requests.get(f"{CATEGORY_SERVICE_URL}/{category_id}")
        return response.status_code == 200
