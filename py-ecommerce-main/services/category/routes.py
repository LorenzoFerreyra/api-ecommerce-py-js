from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from .models import Category, CategorySchema
from .service import CategoryService
from .db import get_session

router = APIRouter()


@router.get("/", response_model=list[Category])
def get_categories(session: Session = Depends(get_session)):
    service = CategoryService(session)
    return service.get_all()


@router.get("/{category_id}")
def get_category(category_id: UUID, session: Session = Depends(get_session)):
    service = CategoryService(session)
    category = service.get_one(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    products = service.get_products(category_id)
    return {"category": category, "products": products}


@router.post("/", response_model=Category)
def create_category(category: CategorySchema, session: Session = Depends(get_session)):
    category = Category(name=category.name.lower().strip())
    service = CategoryService(session)
    return service.create(category)


@router.put("/{category_id}", response_model=Category)
def update_category(
    category_id: UUID, category: CategorySchema, session: Session = Depends(get_session)
):
    service = CategoryService(session)
    updated_category = service.update(category_id, category)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category


@router.delete("/{category_id}")
def delete_category(category_id: UUID, session: Session = Depends(get_session)):
    service = CategoryService(session)
    try:
        deleted = service.delete(category_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": "Category deleted successfully", "deleted": deleted}
