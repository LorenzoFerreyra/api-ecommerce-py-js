from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Body
from sqlmodel import Session
from .models import Order, OrderSchema
from .service import OrderService
from .db import get_session

router = APIRouter()


@router.get("/user/{user_id}", response_model=list[Order])
def get_orders(user_id: UUID, session: Session = Depends(get_session)):
    service = OrderService(session)
    return service.get_all(user_id)


@router.get("/{order_id}")
def get_order(order_id: UUID, session: Session = Depends(get_session)):
    service = OrderService(session)
    order = service.get_one(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.post("/", response_model=Order)
def create_order(
    order: OrderSchema,
    products: dict[UUID, int] = Body(),
    session: Session = Depends(get_session),
):
    service = OrderService(session)
    try:
        order = service.create(order, products)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return order
