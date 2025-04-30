from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Body
from sqlmodel import Session
from .service import UserService
from .db import get_session

router = APIRouter()


@router.get("/{user_id}")
def get_user(user_id: UUID, session: Session = Depends(get_session)):
    service = UserService(session)
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/login")
def login(
    email: str = Body(), password: str = Body(), session: Session = Depends(get_session)
):
    service = UserService(session)
    user = service.get_user(email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
