# Home' Kitchen - Python FastAPI Backend

A modern, fast, and scalable backend API for the Home' Kitchen restaurant built with Python FastAPI.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs with Python
- **PostgreSQL Database**: Robust relational database with SQLAlchemy ORM
- **Automatic API Documentation**: Interactive API docs with Swagger UI
- **Email Notifications**: Automated email sending for orders and applications
- **File Upload Support**: Resume uploads for career applications
- **CORS Support**: Cross-origin resource sharing enabled
- **Type Safety**: Full type hints and Pydantic validation
- **Async Support**: High-performance async/await operations

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Email**: emails library
- **File Upload**: FastAPI UploadFile
- **Documentation**: Auto-generated OpenAPI/Swagger

## 📋 Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- pip (Python package manager)

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Navigate to the project directory
cd Restaurant

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup

1. Create a PostgreSQL database named `homekitchen`
2. Update the database connection in `env.example` and rename to `.env`
3. The database tables will be created automatically on first run

### 4. Environment Configuration

Copy `env.example` to `.env` and update the values:

```bash
cp env.example .env
```

Edit `.env` with your database and email credentials:

```env
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=homekitchen
DB_USER=postgres
DB_PASSWORD=your_password

# Email (Gmail)
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password
ADMIN_EMAIL=admin@homekitchen.com
```

### 5. Start the Server

#### Option 1: Using the batch file (Windows)
```bash
start-python.bat
```

#### Option 2: Manual start
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 6. Access the API

- **API Base URL**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/health

## 📚 API Endpoints

### Menu
- `GET /api/menu` - Get all menu items
- `GET /api/menu/{category}` - Get menu items by category
- `GET /api/menu/categories` - Get all categories

### Orders
- `POST /api/orders` - Place a new order
- `GET /api/orders/{order_id}` - Get order status
- `PUT /api/orders/{order_id}/status` - Update order status

### Careers
- `POST /api/careers` - Submit job application
- `GET /api/careers/applications` - Get all applications (admin)
- `PUT /api/careers/applications/{id}/status` - Update application status

### Contact
- `POST /api/contact` - Submit contact message
- `GET /api/contact/messages` - Get all messages (admin)

### Newsletter
- `POST /api/newsletter` - Subscribe to newsletter
- `DELETE /api/newsletter/{email}` - Unsubscribe
- `GET /api/newsletter/subscribers` - Get subscribers (admin)

## 🗄️ Database Schema

The API automatically creates these tables:

- **menu_items**: Restaurant menu items
- **orders**: Customer orders
- **order_items**: Individual items in orders
- **career_applications**: Job applications
- **contact_messages**: Contact form submissions
- **newsletter_subscribers**: Newsletter subscriptions

## 📧 Email Configuration

To enable email notifications:

1. Use a Gmail account
2. Enable 2-factor authentication
3. Generate an App Password
4. Update `.env` with your credentials

## 🔧 Development

### Project Structure
```
app/
├── __init__.py
├── main.py              # FastAPI application
├── config.py            # Configuration settings
├── database.py          # Database connection
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── init_data.py         # Sample data initialization
├── routers/             # API route handlers
│   ├── menu.py
│   ├── orders.py
│   ├── careers.py
│   ├── contact.py
│   └── newsletter.py
└── utils/               # Utility functions
    └── email_service.py
```

### Adding New Endpoints

1. Create a new router in `app/routers/`
2. Add the router to `app/main.py`
3. Update schemas if needed
4. Test with the interactive docs

### Database Migrations

The current setup uses SQLAlchemy's `create_all()` for simplicity. For production, consider using Alembic for database migrations.

## 🧪 Testing

Test the API using the interactive documentation at `/docs` or with tools like:

- **Postman**: API testing and development
- **curl**: Command-line testing
- **FastAPI TestClient**: Automated testing

## 🚀 Production Deployment

For production deployment:

1. Use a production ASGI server like Gunicorn
2. Set up proper environment variables
3. Configure reverse proxy (Nginx)
4. Set up SSL certificates
5. Use production database
6. Configure logging and monitoring

## 📝 License

This project is part of the Home' Kitchen restaurant management system.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For support or questions, please contact the development team.

---

**Happy Coding! 🎉**
