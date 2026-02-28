from fastapi import APIRouter, HTTPException
from schemas.product_schema import ProductCreate
from model.product import products_db, product_id_counter

router = APIRouter()

# Create product
@router.post("/products/")
def create_product(product: ProductCreate):
    global product_id_counter
    new_product = {
        "id": product_id_counter,
        "name": product.name,
        "price": product.price
    }
    products_db.append(new_product)
    product_id_counter += 1
    return new_product


# Get all products
@router.get("/products/")
def get_products():
    return products_db


# Get product by id
@router.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
