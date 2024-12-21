from pymongo.collection import Collection
from sqlalchemy.orm import Session

def get_paginated_products(collection: Collection, filters: dict, page: int, limit: int):
    query = {}
    if "category" in filters:
        query["category.main_category"] = filters["category"]
    skip = (page - 1) * limit
    total_count = collection.count_documents(query)
    products = list(collection.find(query).skip(skip).limit(limit))
    return products, total_count

def get_product_details(collection: Collection, product_id: str, pg_session: Session):
    product = collection.find_one({"_id": product_id})
    if not product:
        return None
    reviews = pg_session.execute(
        "SELECT reviewer_name, rating, comment FROM reviews WHERE product_id = :id",
        {"id": product_id}
    ).fetchall()
    product["reviews"] = [{"reviewer_name": r[0], "rating": r[1], "comment": r[2]} for r in reviews]
    return product

def add_review(db: Session, review: dict):
    db.execute(
        "INSERT INTO reviews (product_id, reviewer_name, rating, comment) VALUES (:product_id, :reviewer_name, :rating, :comment)",
        review
    )
    db.commit()
