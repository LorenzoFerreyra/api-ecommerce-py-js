from uuid import UUID
import requests
from sqlmodel import Session, select
from .models import Category, CategorySchema

PRODUCT_SERVICE_URL = "http://product:8001"


class CategoryService:
    def __init__(self, session: Session):
        self.session = session

    def get_one(self, category_id: UUID) -> Category | None:
        return self.session.get(Category, category_id)

    def get_products(self, category_id: UUID) -> list[Category]:
        url = f"{PRODUCT_SERVICE_URL}/category/{category_id}"
        response = requests.get(url)
        return response.json()

    def get_all(self) -> list[Category]:
        statement = select(Category)
        return self.session.exec(statement).all()

    def create(self, category: Category) -> Category:
        self.session.add(category)
        self.session.commit()
        self.session.refresh(category)
        return category

    def update(
        self, category_id: UUID, category_data: CategorySchema
    ) -> Category | None:
        category = self.get_one(category_id)
        if category:
            category.name = category_data.name
            self.session.commit()
            self.session.refresh(category)
        return category

    def delete(self, category_id: UUID) -> bool:
        category = self.get_one(category_id)
        if category:
            url = f"{PRODUCT_SERVICE_URL}/category/{category_id}"
            response = requests.delete(url)
            self.session.delete(category)
            self.session.commit()
            return {"category": category, "colateral": response.json()}
        raise ValueError("Category not found")
