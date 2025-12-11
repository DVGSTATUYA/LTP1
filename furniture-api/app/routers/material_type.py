from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/material-type", tags=["MaterialType"])

@router.get("/", response_model=list[schemas.MaterialTypeOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.MaterialType).all()

@router.post("/", response_model=schemas.MaterialTypeOut)
def create(data: schemas.MaterialTypeCreate, db: Session = Depends(get_db)):
    item = models.MaterialType(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
