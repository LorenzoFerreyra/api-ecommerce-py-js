from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Body
from sqlmodel import Session
from .db import get_session
from .models import Product, ProductSchema
from .service import ProductService
from uuid import UUID

router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
def get_products(session: Session = Depends(get_session)):
    service = ProductService(session)
    return service.get_all()


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: UUID, session: Session = Depends(get_session)):
    service = ProductService(session)
    product = service.get_one(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/category/{category_id}", response_model=list[Product])
def get_products_by_category(
    category_id: UUID, session: Session = Depends(get_session)
):
    service = ProductService(session)
    try:
        products = service.get_by_category(category_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return products


@router.post("/")
def create_product(product: ProductSchema, session: Session = Depends(get_session)):
    service = ProductService(session)
    try:
        new_product = service.create(product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return new_product


@router.patch("/stock", response_model=Product)
def update_stock(
    product_id: UUID = Body(),
    stock: int = Body(),
    session: Session = Depends(get_session),
):
    service = ProductService(session)
    try:
        product = service.update_stock(product_id, stock)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return product


@router.patch("/", response_model=Product)
def update_category(
    product_id: UUID = Body(),
    category_id: UUID = Body(),
    session: Session = Depends(get_session),
):
    service = ProductService(session)
    try:
        product = service.update_category(product_id, category_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return product


@router.delete("/category/{category_id}")
def delete_category(category_id: UUID, session: Session = Depends(get_session)):
    service = ProductService(session)
    try:
        service.remove_category(category_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"Category removed from all products"}
