from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/product", tags=["Product"])

@router.get("/", response_model=list[schemas.ProductOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@router.post("/", response_model=schemas.ProductOut)
def create(data: schemas.ProductCreate, db: Session = Depends(get_db)):
    item = models.Product(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

