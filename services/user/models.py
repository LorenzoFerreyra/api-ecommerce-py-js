from sqlmodel import Field, SQLModel
import uuid


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(max_length=100, nullable=False)
    email: str = Field(max_length=100, nullable=False, unique=True)
    password: str = Field(nullable=False)
