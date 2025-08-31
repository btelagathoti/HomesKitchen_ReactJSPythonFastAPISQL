from pydantic import BaseModel, EmailStr
from typing import List, Optional
from decimal import Decimal
from datetime import datetime

# Menu Item Schemas
class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    category: str
    image_url: Optional[str] = None
    video_url: Optional[str] = None
    is_available: bool = True

class MenuItemCreate(MenuItemBase):
    pass

class MenuItem(MenuItemBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Order Schemas
class OrderItemBase(BaseModel):
    item_name: str
    quantity: int
    price: Decimal

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    order_id: int
    
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    customer_name: str
    customer_email: EmailStr
    customer_phone: str
    customer_address: str
    total_amount: Decimal
    payment_method: str = "cash"

class OrderCreate(BaseModel):
    customerInfo: dict
    items: List[OrderItemCreate]
    totalAmount: Decimal

class Order(OrderBase):
    id: int
    status: str
    created_at: datetime
    items: List[OrderItem]
    
    class Config:
        from_attributes = True

# Career Application Schemas
class CareerApplicationBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    position: str
    experience: Optional[str] = None
    message: Optional[str] = None

class CareerApplicationCreate(CareerApplicationBase):
    pass

class CareerApplication(CareerApplicationBase):
    id: int
    resume_path: Optional[str] = None
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Contact Message Schemas
class ContactMessageBase(BaseModel):
    name: str
    email: EmailStr
    subject: Optional[str] = None
    message: str

class ContactMessageCreate(ContactMessageBase):
    pass

class ContactMessage(ContactMessageBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Newsletter Subscription Schemas
class NewsletterSubscriptionBase(BaseModel):
    email: EmailStr

class NewsletterSubscriptionCreate(NewsletterSubscriptionBase):
    pass

class NewsletterSubscription(NewsletterSubscriptionBase):
    id: int
    subscribed_at: datetime
    
    class Config:
        from_attributes = True

# Response Schemas
class SuccessResponse(BaseModel):
    success: bool
    message: str

class OrderResponse(BaseModel):
    success: bool
    orderId: int
    message: str
