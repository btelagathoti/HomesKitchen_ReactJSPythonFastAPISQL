from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import NewsletterSubscriber
from ..schemas import NewsletterSubscriptionCreate, SuccessResponse

router = APIRouter()

@router.post("/newsletter", response_model=SuccessResponse)
async def subscribe_to_newsletter(subscription_data: NewsletterSubscriptionCreate, db: Session = Depends(get_db)):
    """Subscribe to newsletter"""
    try:
        # Check if already subscribed
        existing_subscriber = db.query(NewsletterSubscriber).filter(
            NewsletterSubscriber.email == subscription_data.email
        ).first()
        
        if existing_subscriber:
            raise HTTPException(status_code=400, detail="Email already subscribed")
        
        # Create new subscription
        db_subscription = NewsletterSubscriber(
            email=subscription_data.email
        )
        
        db.add(db_subscription)
        db.commit()
        
        return SuccessResponse(
            success=True,
            message="Successfully subscribed to newsletter"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error subscribing to newsletter: {str(e)}")

@router.delete("/newsletter/{email}")
async def unsubscribe_from_newsletter(email: str, db: Session = Depends(get_db)):
    """Unsubscribe from newsletter"""
    try:
        subscriber = db.query(NewsletterSubscriber).filter(
            NewsletterSubscriber.email == email
        ).first()
        
        if not subscriber:
            raise HTTPException(status_code=404, detail="Email not found in subscribers")
        
        db.delete(subscriber)
        db.commit()
        
        return SuccessResponse(
            success=True,
            message="Successfully unsubscribed from newsletter"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error unsubscribing from newsletter: {str(e)}")

@router.get("/newsletter/subscribers")
async def get_newsletter_subscribers(db: Session = Depends(get_db)):
    """Get all newsletter subscribers (admin only)"""
    try:
        subscribers = db.query(NewsletterSubscriber).order_by(NewsletterSubscriber.subscribed_at.desc()).all()
        return subscribers
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching subscribers: {str(e)}")
