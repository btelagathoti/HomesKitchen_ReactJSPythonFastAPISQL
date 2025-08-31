from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import Optional
import os
from pathlib import Path
from ..database import get_db
from ..models import CareerApplication
from ..schemas import CareerApplicationCreate, SuccessResponse
from ..utils.email_service import EmailService
from ..config import settings

router = APIRouter()
email_service = EmailService()

@router.post("/careers", response_model=SuccessResponse)
async def submit_career_application(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    position: str = Form(...),
    experience: Optional[str] = Form(None),
    message: Optional[str] = Form(None),
    resume: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    """Submit a career application"""
    try:
        resume_path = None
        
        # Handle resume upload if provided
        if resume:
            # Validate file type
            allowed_types = ["application/pdf", "application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
            if resume.content_type not in allowed_types:
                raise HTTPException(status_code=400, detail="Only PDF, DOC, and DOCX files are allowed")
            
            # Validate file size (5MB limit)
            if resume.size > settings.max_file_size:
                raise HTTPException(status_code=400, detail="File size must be less than 5MB")
            
            # Save file
            upload_dir = Path(settings.upload_dir)
            upload_dir.mkdir(exist_ok=True)
            
            filename = f"{int(os.urandom(8).hex(), 16)}-{resume.filename}"
            file_path = upload_dir / filename
            
            with open(file_path, "wb") as buffer:
                content = await resume.read()
                buffer.write(content)
            
            resume_path = str(file_path)
        
        # Create career application
        db_application = CareerApplication(
            name=name,
            email=email,
            phone=phone,
            position=position,
            experience=experience,
            message=message,
            resume_path=resume_path,
            status="pending"
        )
        
        db.add(db_application)
        db.commit()
        
        # Send confirmation email to applicant
        email_service.send_career_confirmation(email, position)
        
        # Send notification email to admin
        admin_subject = "New Career Application - Home' Kitchen"
        admin_html = f"""
        <h2>New Job Application Received</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Phone:</strong> {phone}</p>
        <p><strong>Position:</strong> {position}</p>
        <p><strong>Experience:</strong> {experience or 'Not specified'}</p>
        <p><strong>Message:</strong> {message or 'No message'}</p>
        <p><strong>Resume:</strong> {resume_path or 'Not provided'}</p>
        """
        email_service.send_admin_notification(admin_subject, admin_html)
        
        return SuccessResponse(
            success=True,
            message="Application submitted successfully"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error submitting application: {str(e)}")

@router.get("/careers/applications")
async def get_career_applications(db: Session = Depends(get_db)):
    """Get all career applications (admin only)"""
    try:
        applications = db.query(CareerApplication).order_by(CareerApplication.created_at.desc()).all()
        return applications
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching applications: {str(e)}")

@router.put("/careers/applications/{application_id}/status")
async def update_application_status(
    application_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    """Update application status (admin only)"""
    try:
        application = db.query(CareerApplication).filter(CareerApplication.id == application_id).first()
        
        if not application:
            raise HTTPException(status_code=404, detail="Application not found")
            
        application.status = status
        db.commit()
        
        return {"success": True, "message": f"Application status updated to {status}"}
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating application status: {str(e)}")
