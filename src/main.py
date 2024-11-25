from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.profile_management.router import router as profile_router
from src.address_management.router import router as address_router
from src.order_management.router import router as order_router
from src.payments_management.router import router as payments_router
from src.product_management.router import router as product_router
from src.wishlist.router import router as wishlist_router
from src.authentication.router import router as auth_router

app = FastAPI()

# CORS Middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with your frontend's URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root Endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the app backend!"}

# Include Routers for Modular Endpoints
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(profile_router, prefix="/profile", tags=["Profile Management"])
app.include_router(address_router, prefix="/address", tags=["Address Management"])
app.include_router(order_router, prefix="/orders", tags=["Order Management"])
app.include_router(payments_router, prefix="/payments", tags=["Payments Management"])
app.include_router(product_router, prefix="/products", tags=["Product Management"])
app.include_router(wishlist_router, prefix="/wishlist", tags=["Wishlist"])
