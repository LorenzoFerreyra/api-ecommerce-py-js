from fastapi import APIRouter, HTTPException
import requests

router = APIRouter(prefix="/api/v1")

PRODUCT_SERVICE_URL = "http://product:8001"
CATEGORY_SERVICE_URL = "http://category:8002"
USER_SERVICE_URL = "http://user:8003"
ORDER_SERVICE_URL = "http://order:8004"

"""
Routes requests to the Product Microservice.
"""


@router.get("/products/{path:path}")
async def route_to_product_service(path: str):
    try:
        print(path)
        print(f"{PRODUCT_SERVICE_URL}/{path}")
        response = requests.get(f"{PRODUCT_SERVICE_URL}/{path}")
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/products/{path:path}")
async def route_to_product_service(path: str, payload: dict):
    try:
        response = requests.post(f"{PRODUCT_SERVICE_URL}/{path}", json=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/products/{path:path}")
async def route_to_product_service(path: str, payload: dict):
    try:
        response = requests.patch(f"{PRODUCT_SERVICE_URL}/{path}", json=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/products/{path:path}")
async def route_to_product_service(path: str):
    try:
        response = requests.delete(f"{PRODUCT_SERVICE_URL}/{path}")
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


"""
Routes requests to the Category Microservice.
"""


@router.get("/categories/{path:path}")
async def route_to_category_service(path: str):
    try:
        response = requests.get(f"{CATEGORY_SERVICE_URL}/{path}")
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/categories/{path:path}")
async def route_to_category_service(path: str, payload: dict):
    try:
        response = requests.post(f"{CATEGORY_SERVICE_URL}/{path}", json=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/categories/{path:path}")
async def route_to_category_service(path: str, payload: dict):
    try:
        response = requests.put(f"{CATEGORY_SERVICE_URL}/{path}", json=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/categories/{path:path}")
async def route_to_category_service(path: str):
    try:
        response = requests.delete(f"{CATEGORY_SERVICE_URL}/{path}")
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


"""
Routes requests to the User Microservice.
"""


@router.get("/users/{path:path}")
async def route_to_user_service(path: str):
    try:
        response = requests.get(f"{USER_SERVICE_URL}/{path}")
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/users/{path:path}")
async def route_to_user_service(path: str, payload: dict):
    try:
        response = requests.post(f"{USER_SERVICE_URL}/{path}", json=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


"""
Routes requests to the User Microservice.
"""


@router.get("/users/{path:path}")
async def route_to_user_service(path: str):
    try:
        response = requests.get(f"{USER_SERVICE_URL}/{path}")
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/users/{path:path}")
async def route_to_user_service(path: str, payload: dict):
    try:
        response = requests.post(f"{USER_SERVICE_URL}/{path}", json=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


"""
Routes requests to the Order Microservice.
"""


@router.get("/orders/{path:path}")
async def route_to_order_service(path: str):
    try:
        response = requests.get(f"{ORDER_SERVICE_URL}/{path}")
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/orders/{path:path}")
async def route_to_order_service(path: str, payload: dict):
    try:
        response = requests.post(f"{ORDER_SERVICE_URL}/{path}", json=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
