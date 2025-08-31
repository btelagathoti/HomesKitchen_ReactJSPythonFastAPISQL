import emails
from emails.template import JinjaTemplate
from ..config import settings
import os
from pathlib import Path

class EmailService:
    def __init__(self):
        self.smtp_host = "smtp.gmail.com"
        self.smtp_port = 587
        self.username = settings.email_user
        self.password = settings.email_pass
        self.from_email = settings.email_user or "noreply@homekitchen.com"
        
    def send_email(self, to_email: str, subject: str, html_content: str):
        """Send an email using SMTP"""
        if not self.username or not self.password:
            print("Email credentials not configured. Skipping email send.")
            return False
            
        try:
            message = emails.Message(
                subject=subject,
                html=html_content,
                mail_from=self.from_email
            )
            
            response = message.send(
                to=to_email,
                smtp={
                    "host": self.smtp_host,
                    "port": self.smtp_port,
                    "user": self.username,
                    "password": self.password,
                    "tls": True
                }
            )
            
            if response.status_code == 250:
                print(f"Email sent successfully to {to_email}")
                return True
            else:
                print(f"Failed to send email to {to_email}. Status: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def send_order_confirmation(self, customer_email: str, order_id: int, total_amount: float):
        """Send order confirmation email"""
        subject = "Order Confirmation - Home' Kitchen"
        html_content = f"""
        <h2>Thank you for your order!</h2>
        <p>Order ID: {order_id}</p>
        <p>Total Amount: ${total_amount}</p>
        <p>We'll start preparing your order right away. Estimated delivery time: 30-45 minutes.</p>
        <p>If you have any questions, please call us at +1 (555) 123-4567</p>
        """
        return self.send_email(customer_email, subject, html_content)
    
    def send_career_confirmation(self, applicant_email: str, position: str):
        """Send career application confirmation email"""
        subject = "Application Received - Home' Kitchen"
        html_content = f"""
        <h2>Thank you for your application!</h2>
        <p>We have received your application for the position of <strong>{position}</strong>.</p>
        <p>Our team will review your application and get back to you within 5-7 business days.</p>
        <p>If you have any questions, please email us at careers@homekitchen.com</p>
        """
        return self.send_email(applicant_email, subject, html_content)
    
    def send_admin_notification(self, subject: str, html_content: str):
        """Send notification email to admin"""
        if settings.admin_email:
            return self.send_email(settings.admin_email, subject, html_content)
        return False
