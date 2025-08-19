# 🧪 Testing Guide for Library Management System

This guide provides comprehensive testing instructions for the Django admin to DRF + Vue.js migration project.

## 🚀 Quick Start Testing

### Prerequisites
- Python 3.8+
- Node.js 16+
- All dependencies installed (see setup instructions)

### 1. Backend Testing (Django + DRF)

#### Start the Django Server
```bash
# Terminal 1: Start Django server
python3 manage.py runserver
```

#### Test API Endpoints (Unauthenticated)
```bash
# Terminal 2: Test with unauthenticated access
DJANGO_SETTINGS_MODULE=library_management.settings_test python3 manage.py runserver 8001
python3 test_api.py
```

#### Test API Endpoints (Authenticated)
```bash
# Terminal 2: Test with authentication
python3 test_api_with_auth.py
```

### 2. Frontend Testing (Vue.js)

#### Start the Vue.js Development Server
```bash
# Terminal 3: Start Vue.js server
npm run dev
```

#### Access the Frontend
- Open your browser to `http://localhost:3000`
- The Vue.js admin panel should load

## 📋 Detailed Testing Steps

### Step 1: Verify Backend Setup

1. **Check Django Server**
   ```bash
   curl http://localhost:8000/admin/
   ```
   Should return the Django admin login page.

2. **Check API Endpoints** (with test settings)
   ```bash
   # Start server with test settings
   DJANGO_SETTINGS_MODULE=library_management.settings_test python3 manage.py runserver 8001
   
   # Test API endpoints
   curl http://localhost:8001/api/book-loans/
   curl http://localhost:8001/api/students/
   curl http://localhost:8001/api/books/
   curl http://localhost:8001/api/book-loans/statistics/
   ```

### Step 2: Test Database and Sample Data

1. **Verify Sample Data**
   ```bash
   python3 manage.py shell
   ```
   
   In the Django shell:
   ```python
   from library.models import Student, Book, BookLoan
   
   # Check students
   print(f"Students: {Student.objects.count()}")
   print(f"Books: {Book.objects.count()}")
   print(f"Book Loans: {BookLoan.objects.count()}")
   
   # Check specific data
   for student in Student.objects.all()[:3]:
       print(f"- {student.name} ({student.student_id})")
   
   for book in Book.objects.all()[:3]:
       print(f"- {book.title} by {book.author}")
   
   for loan in BookLoan.objects.all()[:3]:
       print(f"- {loan.student.name} borrowed {loan.book.title}")
   
   exit()
   ```

### Step 3: Test API Functionality

#### Test CRUD Operations

1. **Create a New Book Loan**
   ```bash
   curl -X POST http://localhost:8001/api/book-loans/ \
     -H "Content-Type: application/json" \
     -d '{
       "student_id": 1,
       "book_id": 1,
       "due_date": "2024-02-15T00:00:00Z"
     }'
   ```

2. **Get All Book Loans**
   ```bash
   curl http://localhost:8001/api/book-loans/
   ```

3. **Filter Book Loans**
   ```bash
   # Filter by student name
   curl "http://localhost:8001/api/book-loans/?student_name=Alice"
   
   # Filter by book title
   curl "http://localhost:8001/api/book-loans/?book_title=Gatsby"
   
   # Filter by status
   curl "http://localhost:8001/api/book-loans/?is_returned=false"
   ```

4. **Mark a Book as Returned**
   ```bash
   curl -X POST http://localhost:8001/api/book-loans/1/mark_as_returned/
   ```

5. **Get Statistics**
   ```bash
   curl http://localhost:8001/api/book-loans/statistics/
   ```

#### Test Custom Actions

1. **Get Overdue Loans**
   ```bash
   curl http://localhost:8001/api/book-loans/overdue_loans/
   ```

2. **Get Active Loans**
   ```bash
   curl http://localhost:8001/api/book-loans/active_loans/
   ```

### Step 4: Test Frontend Integration

1. **Start Both Servers**
   ```bash
   # Terminal 1: Django server (with test settings)
   DJANGO_SETTINGS_MODULE=library_management.settings_test python3 manage.py runserver 8001
   
   # Terminal 2: Vue.js server
   npm run dev
   ```

2. **Test Frontend Features**
   - Open `http://localhost:3000` in your browser
   - Verify the statistics dashboard loads
   - Test filtering functionality
   - Test creating a new book loan
   - Test editing an existing loan
   - Test marking a book as returned
   - Test deleting a loan

### Step 5: Test Authentication (Optional)

1. **Test with Authentication**
   ```bash
   # Start normal Django server
   python3 manage.py runserver
   
   # Login to Django admin
   # Go to http://localhost:8000/admin/
   # Login with username: admin, password: (you set this)
   
   # Test API endpoints (should work after login)
   curl http://localhost:8000/api/book-loans/
   ```

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Find and kill process using port 8000
   lsof -ti:8000 | xargs kill -9
   
   # Or use a different port
   python3 manage.py runserver 8001
   ```

2. **Database Errors**
   ```bash
   # Reset database
   rm db.sqlite3
   python3 manage.py migrate
   python3 seed_data.py
   ```

3. **CORS Errors**
   - Check that CORS settings are correct in `settings.py`
   - Ensure frontend is running on allowed origins

4. **Authentication Errors**
   - Use test settings for unauthenticated testing
   - Or login to Django admin first

5. **Vue.js Build Errors**
   ```bash
   # Clear node modules and reinstall
   rm -rf node_modules package-lock.json
   npm install
   ```

### Debug Mode

1. **Django Debug**
   ```python
   # In settings.py
   DEBUG = True
   ```

2. **Vue.js Debug**
   - Open browser developer tools
   - Check console for JavaScript errors
   - Check Network tab for API calls

## 📊 Expected Test Results

### API Endpoints Should Return:

1. **GET /api/book-loans/**
   ```json
   [
     {
       "id": 1,
       "student": {"id": 1, "name": "Alice Johnson", "student_id": "STU001"},
       "book": {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
       "loan_date": "2024-01-15T10:00:00Z",
       "due_date": "2024-01-22T10:00:00Z",
       "return_date": null,
       "is_returned": false
     }
   ]
   ```

2. **GET /api/book-loans/statistics/**
   ```json
   {
     "total_loans": 7,
     "active_loans": 3,
     "overdue_loans": 2,
     "returned_loans": 2
   }
   ```

### Frontend Should Display:

1. **Statistics Dashboard**
   - Total loans count
   - Active loans count
   - Overdue loans count
   - Returned loans count

2. **Book Loans Table**
   - Student name
   - Book title
   - Loan date
   - Due date
   - Return date
   - Status (Active/Returned/Overdue)
   - Action buttons

3. **Filtering Options**
   - Filter by student name
   - Filter by book title
   - Filter by status

## ✅ Success Criteria

The implementation is successful if:

1. ✅ **Backend API works** - All endpoints return correct data
2. ✅ **Frontend loads** - Vue.js admin panel displays correctly
3. ✅ **CRUD operations work** - Create, read, update, delete book loans
4. ✅ **Filtering works** - Filter by student, book, status
5. ✅ **Statistics work** - Dashboard shows correct counts
6. ✅ **Responsive design** - Works on desktop and mobile
7. ✅ **Error handling** - Graceful error messages
8. ✅ **Authentication** - Proper security (when enabled)

## 🎯 Performance Testing

### Load Testing (Optional)

```bash
# Install Apache Bench
brew install httpd

# Test API performance
ab -n 100 -c 10 http://localhost:8001/api/book-loans/
```

### Memory Usage

```bash
# Monitor Django process
ps aux | grep python3

# Monitor Node.js process
ps aux | grep node
```

## 📝 Test Report Template

After testing, document your results:

```markdown
## Test Report

### Environment
- Python: 3.11.7
- Node.js: v22.15.1
- Django: 4.2.7
- Vue.js: 3.3.4

### Test Results
- [ ] Backend API endpoints working
- [ ] Frontend Vue.js component loading
- [ ] CRUD operations functional
- [ ] Filtering working correctly
- [ ] Statistics dashboard accurate
- [ ] Responsive design working
- [ ] Error handling implemented
- [ ] Authentication working

### Issues Found
- None / List any issues here

### Recommendations
- Any suggestions for improvement
```

This testing guide should help you thoroughly test all aspects of the Django admin to DRF + Vue.js migration project!
