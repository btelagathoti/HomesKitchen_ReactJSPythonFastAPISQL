from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import MenuItem
from decimal import Decimal

def init_menu_data():
    """Initialize the database with sample menu data"""
    db = SessionLocal()
    
    try:
        # Check if menu items already exist
        existing_items = db.query(MenuItem).count()
        if existing_items > 0:
            print("Menu data already exists, skipping initialization")
            return
        
        # Sample menu items
        menu_items = [
            # Starters & Snacks
            MenuItem(
                name="Samosas",
                description="Crispy pastry filled with spiced potatoes and peas",
                price=Decimal("8.99"),
                category="Starters & Snacks",
                image_url="🍛",
                is_available=True
            ),
            MenuItem(
                name="Chicken 65",
                description="Spicy deep-fried chicken with curry leaves",
                price=Decimal("12.99"),
                category="Starters & Snacks",
                image_url="🍗",
                is_available=True
            ),
            MenuItem(
                name="Paneer 65",
                description="Spicy deep-fried paneer with curry leaves",
                price=Decimal("10.99"),
                category="Starters & Snacks",
                image_url="🧀",
                is_available=True
            ),
            
            # Main Dishes
            MenuItem(
                name="Butter Chicken",
                description="Tender chicken in rich tomato and butter gravy",
                price=Decimal("18.99"),
                category="Main Dishes",
                image_url="🍗",
                is_available=True
            ),
            MenuItem(
                name="Biryani",
                description="Fragrant rice with tender meat and aromatic spices",
                price=Decimal("22.99"),
                category="Main Dishes",
                image_url="🍚",
                is_available=True
            ),
            MenuItem(
                name="Rogan Josh",
                description="Tender lamb in aromatic Kashmiri spices",
                price=Decimal("24.99"),
                category="Main Dishes",
                image_url="🍖",
                is_available=True
            ),
            MenuItem(
                name="Matar Paneer",
                description="Fresh peas and cottage cheese in tomato gravy",
                price=Decimal("16.99"),
                category="Main Dishes",
                image_url="🥘",
                is_available=True
            ),
            
            # Breads
            MenuItem(
                name="Naan",
                description="Soft leavened bread baked in tandoor",
                price=Decimal("3.99"),
                category="Breads",
                image_url="🫓",
                is_available=True
            ),
            MenuItem(
                name="Roti",
                description="Whole wheat flatbread",
                price=Decimal("2.99"),
                category="Breads",
                image_url="🫓",
                is_available=True
            ),
            MenuItem(
                name="Garlic Naan",
                description="Naan bread topped with garlic and herbs",
                price=Decimal("4.99"),
                category="Breads",
                image_url="🫓",
                is_available=True
            ),
            
            # Sides
            MenuItem(
                name="Basmati Rice",
                description="Fragrant long-grain rice",
                price=Decimal("4.99"),
                category="Sides",
                image_url="🍚",
                is_available=True
            ),
            MenuItem(
                name="Jeera Rice",
                description="Rice flavored with cumin seeds",
                price=Decimal("5.99"),
                category="Sides",
                image_url="🍚",
                is_available=True
            ),
            MenuItem(
                name="Potato Curry",
                description="Spiced potatoes in tomato gravy",
                price=Decimal("6.99"),
                category="Sides",
                image_url="🥔",
                is_available=True
            )
        ]
        
        # Add all menu items
        for item in menu_items:
            db.add(item)
        
        db.commit()
        print(f"✅ Successfully initialized {len(menu_items)} menu items")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error initializing menu data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_menu_data()
