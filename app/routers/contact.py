from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import ContactMessage
from ..schemas import ContactMessageCreate, SuccessResponse
from ..utils.email_service import EmailService

router = APIRouter()
email_service = EmailService()

@router.post("/contact", response_model=SuccessResponse)
async def submit_contact_message(message_data: ContactMessageCreate, db: Session = Depends(get_db)):
    """Submit a contact message"""
    try:
        # Create contact message
        db_message = ContactMessage(
            name=message_data.name,
            email=message_data.email,
            subject=message_data.subject,
            message=message_data.message
        )
        
        db.add(db_message)
        db.commit()
        
        # Send notification email to admin
        admin_subject = "New Contact Message - Home' Kitchen"
        admin_html = f"""
        <h2>New Contact Message</h2>
        <p><strong>Name:</strong> {message_data.name}</p>
        <p><strong>Email:</strong> {message_data.email}</p>
        <p><strong>Subject:</strong> {message_data.subject or 'No subject'}</p>
        <p><strong>Message:</strong></p>
        <p>{message_data.message}</p>
        """
        email_service.send_admin_notification(admin_subject, admin_html)
        
        # Send confirmation email to customer
        customer_subject = "Message Received - Home' Kitchen"
        customer_html = f"""
        <h2>Thank you for your message!</h2>
        <p>We have received your message and will get back to you within 24 hours.</p>
        <p>If you need immediate assistance, please call us at +1 (555) 123-4567</p>
        """
        email_service.send_email(message_data.email, customer_subject, customer_html)
        
        return SuccessResponse(
            success=True,
            message="Message sent successfully"
        )
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error sending message: {str(e)}")

@router.get("/contact/messages")
async def get_contact_messages(db: Session = Depends(get_db)):
    """Get all contact messages (admin only)"""
    try:
        messages = db.query(ContactMessage).order_by(ContactMessage.created_at.desc()).all()
        return messages
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching messages: {str(e)}")
