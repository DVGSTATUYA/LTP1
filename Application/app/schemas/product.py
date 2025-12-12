from pydantic import BaseModel
from typing import Optional

class ProductItem(BaseModel):
    id: int | None
    product_type: str
    product_name: str
    article: int | None
    min_partner_cost: float | None
    main_material: str
    manufacturing_time: int  

class ProductCreate(BaseModel):
    id: int | None
    product_type: str
    product_name: str
    article: Optional[int]
    min_partner_cost: Optional[float]
    main_material: str