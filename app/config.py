from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database settings
    database_url: str = "sqlite:///./homekitchen.db"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "homekitchen"
    db_user: str = "postgres"
    db_password: str = "password"
    
    # Email settings
    email_user: Optional[str] = None
    email_pass: Optional[str] = None
    admin_email: str = "admin@homekitchen.com"
    
    # Server settings
    port: int = 8000
    host: str = "0.0.0.0"
    
    # File upload settings
    max_file_size: int = 5 * 1024 * 1024  # 5MB
    upload_dir: str = "uploads"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
