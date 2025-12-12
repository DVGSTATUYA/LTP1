
from pydantic import BaseModel

class MaterialTypeItem(BaseModel):
    id: int
    type_material: str
    loss_percent: float
