from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Order, OrderItem
from ..schemas import OrderCreate, OrderResponse
from ..utils.email_service import EmailService
from decimal import Decimal

router = APIRouter()
email_service = EmailService()

@router.post("/orders", response_model=OrderResponse)
async def place_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    """Place a new order"""
    try:
        # Extract customer info
        customer_info = order_data.customerInfo
        
        # Create order
        db_order = Order(
            customer_name=customer_info["name"],
            customer_email=customer_info["email"],
            customer_phone=customer_info["phone"],
            customer_address=customer_info["address"],
            total_amount=order_data.totalAmount,
            status="pending"
        )
        
        db.add(db_order)
        db.flush()  # Get the order ID
        
        # Create order items
        for item in order_data.items:
            db_order_item = OrderItem(
                order_id=db_order.id,
                item_name=item.item_name,
                quantity=item.quantity,
                price=item.price
            )
            db.add(db_order_item)
        
        db.commit()
        
        # Send confirmation email
        email_service.send_order_confirmation(
            customer_info["email"],
            db_order.id,
            float(order_data.totalAmount)
        )
        
        return OrderResponse(
            success=True,
            orderId=db_order.id,
            message="Order placed successfully"
        )
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error placing order: {str(e)}")

@router.get("/orders/{order_id}")
async def get_order_status(order_id: int, db: Session = Depends(get_db)):
    """Get order status by order ID"""
    try:
        order = db.query(Order).filter(Order.id == order_id).first()
        
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
            
        return order
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching order: {str(e)}")

@router.put("/orders/{order_id}/status")
async def update_order_status(order_id: int, status: str, db: Session = Depends(get_db)):
    """Update order status (admin only)"""
    try:
        order = db.query(Order).filter(Order.id == order_id).first()
        
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
            
        order.status = status
        db.commit()
        
        return {"success": True, "message": f"Order status updated to {status}"}
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating order status: {str(e)}")
