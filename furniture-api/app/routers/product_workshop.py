from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/product-workshop", tags=["ProductWorkshop"])

@router.get("/", response_model=list[schemas.ProductWorkshopOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.ProductWorkshop).all()

@router.post("/", response_model=schemas.ProductWorkshopOut)
def create(data: schemas.ProductWorkshopCreate, db: Session = Depends(get_db)):
    item = models.ProductWorkshop(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
