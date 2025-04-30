from sqlmodel import SQLModel, Field
import uuid


class CategorySchema(SQLModel):
    name: str = Field(max_length=100, unique=True, nullable=False)


class Category(CategorySchema, table=True):
    __tablename__ = "categories"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
