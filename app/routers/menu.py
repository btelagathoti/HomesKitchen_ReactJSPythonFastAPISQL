from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import MenuItem
from ..schemas import MenuItem as MenuItemSchema

router = APIRouter()

@router.get("/menu", response_model=List[MenuItemSchema])
async def get_menu(db: Session = Depends(get_db)):
    """Get all menu items"""
    try:
        menu_items = db.query(MenuItem).filter(MenuItem.is_available == True).order_by(MenuItem.category, MenuItem.name).all()
        return menu_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching menu: {str(e)}")

@router.get("/menu/{category}", response_model=List[MenuItemSchema])
async def get_menu_by_category(category: str, db: Session = Depends(get_db)):
    """Get menu items by category"""
    try:
        menu_items = db.query(MenuItem).filter(
            MenuItem.category == category,
            MenuItem.is_available == True
        ).order_by(MenuItem.name).all()
        
        if not menu_items:
            raise HTTPException(status_code=404, detail=f"No items found for category: {category}")
            
        return menu_items
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching menu by category: {str(e)}")

@router.get("/menu/categories")
async def get_categories(db: Session = Depends(get_db)):
    """Get all available menu categories"""
    try:
        categories = db.query(MenuItem.category).filter(
            MenuItem.is_available == True
        ).distinct().all()
        
        return [category[0] for category in categories]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching categories: {str(e)}")
