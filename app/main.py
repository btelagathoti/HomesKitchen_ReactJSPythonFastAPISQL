from fastapi import FastAPI, HTTPException, Depends, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import uvicorn
from contextlib import asynccontextmanager
import os
from pathlib import Path

from .database import engine, get_db
from .models import Base
from .routers import menu, orders, careers, contact, newsletter
from .config import settings
from .utils.email_service import EmailService
from .init_data import init_menu_data

# Create uploads directory if it doesn't exist
uploads_dir = Path("uploads")
uploads_dir.mkdir(exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    print("🚀 Home' Kitchen FastAPI server starting up...")
    
    # Initialize sample data
    init_menu_data()
    
    yield
    # Shutdown
    print("🛑 Home' Kitchen FastAPI server shutting down...");

app = FastAPI(
    title="Home' Kitchen API",
    description="FastAPI backend for Home' Kitchen restaurant",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files for uploads
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Include routers
app.include_router(menu.router, prefix="/api", tags=["menu"])
app.include_router(orders.router, prefix="/api", tags=["orders"])
app.include_router(careers.router, prefix="/api", tags=["careers"])
app.include_router(contact.router, prefix="/api", tags=["contact"])
app.include_router(newsletter.router, prefix="/api", tags=["newsletter"])

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "OK",
        "message": "Home' Kitchen API is running",
        "version": "1.0.0"
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Home' Kitchen API",
        "docs": "/docs",
        "health": "/api/health"
    }

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
