from sqlalchemy import Column, Integer, String, Enum, Text, DateTime, func
from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(250))
    category = Column(Enum('finished', 'semi-finished', 'raw'))
    sku= Column(String(100))
    product_image  = Column(Text)
    unit_of_measure = Column(Enum('mtr', 'mm', 'ltr', 'ml', 'cm', 'mg', 'gm', 'unit', 'pack'))
    lead_time = Column(Integer) 
    created_date = Column(DateTime, server_default=func.now())
    updated_date = Column(DateTime, server_default=func.now())
