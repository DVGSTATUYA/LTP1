from fastapi import FastAPI
from app.routers import material_type, product, product_type, product_workshop, workshop
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(material_type.router)
app.include_router(product_type.router) 
app.include_router(product_workshop.router)
app.include_router(product.router)
app.include_router(workshop.router)

@app.get("/")
def root():
    return {"message": "Добро пожаловать в API мебельной фабрики!"}