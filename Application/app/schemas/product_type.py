
from pydantic import BaseModel

class ProductTypeItem(BaseModel):
    id: int
    product_type: str
    coefficient: float
