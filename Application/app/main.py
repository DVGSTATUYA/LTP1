from fastapi import FastAPI, HTTPException
from app.schemas.product import ProductItem, ProductCreate
from app.repositories.products_repo import insert_product, update_product, delete_product
from app.services.products_service import list_products_with_time


from app.schemas.product_type import ProductTypeItem
from app.schemas.material_type import MaterialTypeItem
from app.schemas.workshop import WorkshopItem, ProductWorkshopItem
from app.schemas.calc import RawCalcResponse

from app.services.product_types_service import list_product_types
from app.services.material_types_service import list_material_types
from app.services.workshops_service import list_workshops_all, list_workshops_for_product
from app.services.calc_service import calculate_raw_material

app = FastAPI(title="Продукция мебельной компании")

@app.get("/products", response_model=list[ProductItem])
def get_products():
    return list_products_with_time()

@app.post("/products")
def create_product(product: ProductCreate):
    product_id = insert_product(product.dict())
    return {"id": product_id, "message": "Product created successfully"}

@app.put("/products/{product_id}")
def edit_product(product_id: int, product: ProductCreate):
    update_product(product_id, product.dict())
    return {"message": "Product updated successfully"}

@app.delete("/products/{product_id}")
def remove_product(product_id: int):
    delete_product(product_id)
    return {"message": "Product deleted successfully"}

# Справочники
@app.get("/product_types", response_model=list[ProductTypeItem])
def get_product_types():
    return list_product_types()

@app.get("/material_types", response_model=list[MaterialTypeItem])
def get_material_types():
    return list_material_types()

# Цеха
@app.get("/workshops", response_model=list[WorkshopItem])
def get_workshops():
    return list_workshops_all()

@app.get("/products/{product_id}/workshops", response_model=list[ProductWorkshopItem])
def get_product_workshops(product_id: int):
    return list_workshops_for_product(product_id)

# Расчет сырья
@app.get("/calculate_raw_material", response_model=RawCalcResponse)
def calculate_raw_material_endpoint(
    product_type_id: int,
    material_type_id: int,
    quantity: int,
    param1: float,
    param2: float,
):
    result = calculate_raw_material(product_type_id, material_type_id, quantity, param1, param2)
    return {"result": result}
