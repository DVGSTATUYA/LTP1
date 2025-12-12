
from pydantic import BaseModel

class WorkshopItem(BaseModel):
    id: int
    workshop_name: str
    workshop_type: str
    employee_count: int

class ProductWorkshopItem(BaseModel):
    id: int
    workshop_name: str
    employee_count: int
    production_time_h: float
