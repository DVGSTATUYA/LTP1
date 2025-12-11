from pydantic import BaseModel

class MaterialTypeBase(BaseModel):
    name: str
    loss_percent: float

class MaterialTypeCreate(MaterialTypeBase):
    pass

class MaterialTypeOut(MaterialTypeBase):
    id: int

    class Config:
        orm_mode = True

class ProductTypeBase(BaseModel):
    name: str
    coefficient: float

class ProductTypeCreate(ProductTypeBase): pass

class ProductTypeOut(ProductTypeBase):
    id: int
    class Config: from_attributes = True


class ProductWorkshopBase(BaseModel):
    product_name: str
    workshop_name: str
    production_time: float

class ProductWorkshopCreate(ProductWorkshopBase): pass

class ProductWorkshopOut(ProductWorkshopBase):
    id: int
    class Config: from_attributes = True


class ProductBase(BaseModel):
    product_type: str
    product_name: str
    article: int
    min_cost: float
    main_material: str

class ProductCreate(ProductBase): pass

class ProductOut(ProductBase):
    id: int
    class Config: from_attributes = True


class WorkshopBase(BaseModel):
    name: str
    type: str
    people_count: int

class WorkshopCreate(WorkshopBase): pass

class WorkshopOut(WorkshopBase):
    id: int
    class Config: from_attributes = True
