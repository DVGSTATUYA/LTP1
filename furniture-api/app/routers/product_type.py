from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/product-type", tags=["ProductType"])

@router.get("/", response_model=list[schemas.ProductTypeOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.ProductType).all()

@router.post("/", response_model=schemas.ProductTypeOut)
def create(data: schemas.ProductTypeCreate, db: Session = Depends(get_db)):
    item = models.ProductType(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
