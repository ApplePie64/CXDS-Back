from pydantic import BaseModel
from typing import List, Optional

# Product Details Schema
class Product(BaseModel):
    id: str
    name: str
    brand: str
    category: dict
    price: dict
    colors: List[dict]
    images: List[str]
    tags: List[str]

class ProductResponse(Product):
    reviews: Optional[List[dict]]

# Review Input Schema
class ReviewInput(BaseModel):
    product_id: str
    reviewer_name: str
    rating: int
    comment: str

# Paginated Response
class PaginatedResponse(BaseModel):
    total_count: int
    current_page: int
    total_pages: int
    products: List[Product]
