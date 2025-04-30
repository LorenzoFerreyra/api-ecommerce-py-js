from uuid import UUID
from sqlmodel import Session, select
from .models import User


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def get_user(self, email: str, password) -> User | None:
        user = self.session.exec(select(User).where(User.email == email)).first()
        if user and user.password == password:
            return user
        return None

    def get_user_by_id(self, user_id: UUID) -> User | None:
        return self.session.get(User, user_id)
