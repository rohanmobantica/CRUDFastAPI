from pydantic import BaseModel
from typing import Optional
import enum

class ProductCategory(str, enum.Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UnitOfMeasure(str, enum.Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

class ProductBase(BaseModel):
    name: str
    category: ProductCategory
    description: str
    product_image: str
    sku: str
    unit_of_measure: UnitOfMeasure
    lead_time: int
    

class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    name: Optional[str]
    category: Optional[ProductCategory]
    description: Optional[str]
    product_image: Optional[str]
    sku: Optional[str]
    unit_of_measure: Optional[UnitOfMeasure]
    lead_time: Optional[int]

    class Config:
        from_attributes = True