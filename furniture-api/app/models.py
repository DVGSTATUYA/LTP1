from sqlalchemy import Column, Identity, Integer, String, Float
from app.database import Base

class MaterialType(Base):
    __tablename__ = "Material_type_import"

    id = Column(Integer, Identity(start=1), primary_key=True, index=True)
    name = Column("Material type", String, nullable=False)
    loss_percent = Column("Loss percent", Float, nullable=False)

class ProductType(Base):
    __tablename__ = "Product_type_import"

    id = Column(Integer, Identity(start=1), primary_key=True, index=True)
    name = Column("Product type", String, nullable=False)
    coefficient = Column("Product type coefficient", Float, nullable=False)

class ProductWorkshop(Base):
    __tablename__ = "Product_workshops_import"

    id = Column(Integer, Identity(start=1), primary_key=True, index=True)
    product_name = Column("Product name", String, nullable=False)
    workshop_name = Column("Workshop name", String, nullable=False)
    production_time = Column("Production time, h", Float, nullable=False)

class Product(Base):
    __tablename__ = "Products_import"

    id = Column(Integer, Identity(start=1), primary_key=True, index=True)
    product_type = Column("Product type", String, nullable=False)
    product_name = Column("Product name", String, nullable=False)
    article = Column("Article", Integer, nullable=False)
    min_cost = Column("Minimum cost for a partner", Float, nullable=False)
    main_material = Column("Main material", String, nullable=False)

class Workshop(Base):
    __tablename__ = "Workshops_import"

    id = Column(Integer, Identity(start=1), primary_key=True, index=True)
    name = Column("Workshop name", String, nullable=False)
    type = Column("Workshop type", String, nullable=False)
    people_count = Column("Number of people for production", Integer, nullable=False)
