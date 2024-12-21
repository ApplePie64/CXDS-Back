from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from pymongo.database import Database
from product_management.schemas import ProductResponse, ReviewInput, PaginatedResponse
from product_management.dependencies import get_mongo_client, get_pg_session
from product_management.service import get_paginated_products, get_product_details, add_review

router = APIRouter()

@router.get("/products", response_model=PaginatedResponse)
async def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(50, le=100),
    category: str = Query(None),
    db: Database = Depends(get_mongo_client)
):
    collection = db["products"]
    filters = {"category": category} if category else {}
    products, total_count = get_paginated_products(collection, filters, page, limit)
    total_pages = (total_count + limit - 1) // limit
    return {"total_count": total_count, "current_page": page, "total_pages": total_pages, "products": products}

@router.get("/products/{product_id}", response_model=ProductResponse)
async def retrieve_product(product_id: str, db: Database = Depends(get_mongo_client), pg_session: Session = Depends(get_pg_session)):
    collection = db["products"]
    product = get_product_details(collection, product_id, pg_session)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/reviews")
async def add_product_review(review: ReviewInput, db: Session = Depends(get_pg_session)):
    add_review(db, review.dict())
    return {"message": "Review added successfully"}

@router.get("/categories")
async def list_categories(db: Database = Depends(get_mongo_client)):
    collection = db["products"]
    pipeline = [{"$group": {"_id": "$category.main_category", "subcategories": {"$addToSet": "$category.sub_category"}}}]
    categories = list(collection.aggregate(pipeline))
    return {"categories": categories}
