# 📚 Library Management System

A modern, full-stack library management system built with **Django REST Framework** and **Vue.js 3**, featuring a beautiful Tailwind CSS interface and complete CRUD operations.

![Django](https://img.shields.io/badge/Django-4.2+-green.svg)
![Vue.js](https://img.shields.io/badge/Vue.js-3.0+-blue.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-38B2AC.svg)
![Python](https://img.shields.io/badge/Python-3.11+-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

## ✨ Features

- 🚀 **Full CRUD Operations** - Create, Read, Update, Delete book loans
- 🎨 **Beautiful Modern UI** - Vue.js 3 with Tailwind CSS
- 🔌 **RESTful API** - Django REST Framework backend
- 📊 **Real-time Dashboard** - Live statistics and analytics
- 🔍 **Advanced Search & Filter** - Multi-criteria filtering
- 📱 **Responsive Design** - Works perfectly on all devices
- 🔐 **Authentication Ready** - Built-in auth system
- 🧪 **Comprehensive Testing** - Full test coverage
- 🐳 **Docker Ready** - Containerized deployment

## 🛠 Tech Stack

### Backend
- **Django 4.2+** - Web framework
- **Django REST Framework** - API framework
- **SQLite/PostgreSQL** - Database
- **Python 3.11+** - Programming language

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client
- **Vite** - Build tool

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 16+
- npm or yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd library-management-system
   ```

2. **Set up Python virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements/development.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python scripts/seed_data.py
   ```

5. **Install frontend dependencies**
   ```bash
   cd frontend
   npm install
   ```

6. **Start the development servers**
   ```bash
   # Terminal 1: Start Django backend
   python manage.py runserver
   
   # Terminal 2: Start Vue.js frontend
   cd frontend
   npm run dev
   ```

7. **Access the application**
   - 🌐 **Frontend**: http://localhost:3000
   - 🔌 **Backend API**: http://localhost:8000/api/
   - ⚙️ **Django Admin**: http://localhost:8000/admin/

## 📁 Project Structure

```
library-management-system/
├── 📁 apps/                    # Django applications
│   ├── 📁 core/               # Core functionality
│   │   ├── views.py           # API ViewSets
│   │   └── urls.py            # API URL routing
│   └── 📁 library/            # Library models and logic
│       ├── models.py          # Database models
│       ├── serializers.py     # DRF serializers
│       └── admin.py           # Django admin
├── 📁 config/                 # Django configuration
│   ├── 📁 settings/           # Environment-specific settings
│   │   ├── base.py            # Base settings
│   │   ├── development.py     # Development settings
│   │   ├── production.py      # Production settings
│   │   └── test.py            # Test settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
├── 📁 frontend/               # Vue.js frontend
│   ├── 📁 src/
│   │   ├── 📁 pages/          # Vue components
│   │   │   └── AdminBookLoan.vue
│   │   ├── main.js            # Vue app entry point
│   │   └── style.css          # Tailwind CSS
│   ├── index.html             # HTML template
│   ├── package.json           # Node.js dependencies
│   ├── vite.config.js         # Vite configuration
│   └── tailwind.config.js     # Tailwind configuration
├── 📁 requirements/           # Python dependencies
│   ├── base.txt               # Base dependencies
│   ├── development.txt        # Development dependencies
│   ├── production.txt         # Production dependencies
│   └── test.txt               # Test dependencies
├── 📁 scripts/                # Automation scripts
│   ├── setup.sh               # Project setup
│   ├── start_dev.sh           # Start development servers
│   ├── seed_data.py           # Database seeding
│   └── run_tests.sh           # Run tests
├── 📁 tests/                  # Test files
│   ├── test_crud.py           # CRUD operation tests
│   └── test_structure.py      # Project structure tests
├── manage.py                  # Django management script
├── .env.example               # Environment variables template
└── README.md                  # This file
```

## 🔌 API Endpoints

### 📚 Book Loans
- `GET /api/book-loans/` - List all book loans
- `POST /api/book-loans/` - Create a new book loan
- `GET /api/book-loans/{id}/` - Get a specific book loan
- `PATCH /api/book-loans/{id}/` - Update a book loan
- `DELETE /api/book-loans/{id}/` - Delete a book loan
- `POST /api/book-loans/{id}/mark_as_returned/` - Mark book as returned
- `GET /api/book-loans/statistics/` - Get loan statistics

### 👥 Students
- `GET /api/students/` - List all students
- `POST /api/students/` - Create a new student
- `GET /api/students/{id}/` - Get a specific student
- `PATCH /api/students/{id}/` - Update a student
- `DELETE /api/students/{id}/` - Delete a student

### 📖 Books
- `GET /api/books/` - List all books
- `POST /api/books/` - Create a new book
- `GET /api/books/{id}/` - Get a specific book
- `PATCH /api/books/{id}/` - Update a book
- `DELETE /api/books/{id}/` - Delete a book

## 🎯 Features

### 📊 Dashboard Statistics
- 📈 Total loans count
- ⏰ Active loans count
- ⚠️ Overdue loans count
- ✅ Returned loans count

### 🔍 Advanced Filtering
- 🔤 Filter by student name
- 📖 Filter by book title
- 🏷️ Filter by loan status (Active/Returned)
- ⚡ Real-time search

### 📚 Book Management
- 📦 Track available copies
- 🔄 Automatic copy management on loan/return
- 📋 ISBN and publication year tracking

### 👥 Student Management
- 🆔 Student ID tracking
- 📧 Email management
- 📜 Loan history

### 📅 Loan Management
- 📅 Due date tracking
- ⏰ Overdue detection
- 📝 Return date recording
- 🏷️ Status management

## 🧪 Development

### Running Tests
```bash
# Run Django tests
python manage.py test

# Run API tests
python tests/test_crud.py

# Run structure tests
python tests/test_structure.py
```

### Code Quality
```bash
# Format code with black
black .

# Check code style with flake8
flake8 .

# Sort imports with isort
isort .
```

### Database Management
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Seed sample data
python scripts/seed_data.py
```

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3

# Frontend
VITE_API_BASE_URL=http://localhost:8000/api
```

## 🚀 Deployment

### Production Setup
1. Set `DEBUG=False` in production settings
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure environment variables
5. Set up a reverse proxy (nginx)
6. Use Gunicorn for WSGI server

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- 📧 **Email**: support@librarymanagement.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- 📖 **Documentation**: [Wiki](https://github.com/your-repo/wiki)

## 🙏 Acknowledgments

- Django REST Framework team
- Vue.js team
- Tailwind CSS team
- All contributors and supporters

---

**Made with ❤️ by the Library Management Team**
