# Dependencies for product_management
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# MongoDB Connection
def get_mongo_client():
    mongo_uri = os.getenv("MONGODB_URI")
    client = MongoClient(mongo_uri)
    return client[os.getenv("MONGO_DB_NAME")]

# PostgreSQL Connection
DATABASE_URL = os.getenv("SUPABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_pg_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
