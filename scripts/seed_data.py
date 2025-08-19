#!/usr/bin/env python
"""
Data seeding script for the Library Management System.
Run this after setting up the database to populate it with sample data.
"""

import os
import sys
import django
from datetime import datetime, timedelta

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from apps.library.models import Student, Book, BookLoan
from django.utils import timezone


def create_sample_data():
    """Create sample students, books, and book loans for testing."""
    
    print("🌱 Creating sample data...")
    
    # Create students
    students_data = [
        {'name': 'Alice Johnson', 'email': 'alice@university.edu', 'student_id': 'STU001'},
        {'name': 'Bob Smith', 'email': 'bob@university.edu', 'student_id': 'STU002'},
        {'name': 'Carol Davis', 'email': 'carol@university.edu', 'student_id': 'STU003'},
        {'name': 'David Wilson', 'email': 'david@university.edu', 'student_id': 'STU004'},
        {'name': 'Eva Brown', 'email': 'eva@university.edu', 'student_id': 'STU005'},
    ]
    
    students = []
    for data in students_data:
        student, created = Student.objects.get_or_create(
            email=data['email'],
            defaults=data
        )
        students.append(student)
        if created:
            print(f"✅ Created student: {student.name}")
    
    # Create books
    books_data = [
        {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'isbn': '9780743273565', 'published_year': 1925, 'available_copies': 3},
        {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'isbn': '9780446310789', 'published_year': 1960, 'available_copies': 2},
        {'title': '1984', 'author': 'George Orwell', 'isbn': '9780451524935', 'published_year': 1949, 'available_copies': 4},
        {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'isbn': '9780141439518', 'published_year': 1813, 'available_copies': 2},
        {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'isbn': '9780547928241', 'published_year': 1937, 'available_copies': 3},
        {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'isbn': '9780316769488', 'published_year': 1951, 'available_copies': 1},
        {'title': 'Lord of the Flies', 'author': 'William Golding', 'isbn': '9780399501487', 'published_year': 1954, 'available_copies': 2},
        {'title': 'Animal Farm', 'author': 'George Orwell', 'isbn': '9780451526342', 'published_year': 1945, 'available_copies': 3},
    ]
    
    books = []
    for data in books_data:
        book, created = Book.objects.get_or_create(
            isbn=data['isbn'],
            defaults=data
        )
        books.append(book)
        if created:
            print(f"✅ Created book: {book.title}")
    
    # Create book loans
    now = timezone.now()
    
    # Active loans
    active_loans = [
        {'student': students[0], 'book': books[0], 'due_date': now + timedelta(days=7)},
        {'student': students[1], 'book': books[1], 'due_date': now + timedelta(days=14)},
        {'student': students[2], 'book': books[2], 'due_date': now + timedelta(days=3)},
    ]
    
    # Overdue loans
    overdue_loans = [
        {'student': students[3], 'book': books[3], 'due_date': now - timedelta(days=5)},
        {'student': students[4], 'book': books[4], 'due_date': now - timedelta(days=2)},
    ]
    
    # Returned loans
    returned_loans = [
        {'student': students[0], 'book': books[5], 'due_date': now - timedelta(days=10), 'return_date': now - timedelta(days=8), 'is_returned': True},
        {'student': students[1], 'book': books[6], 'due_date': now - timedelta(days=15), 'return_date': now - timedelta(days=12), 'is_returned': True},
    ]
    
    # Create all loans
    all_loans = active_loans + overdue_loans + returned_loans
    
    for loan_data in all_loans:
        # Check if loan already exists
        existing_loan = BookLoan.objects.filter(
            student=loan_data['student'],
            book=loan_data['book'],
            loan_date__date=now.date()
        ).first()
        
        if not existing_loan:
            loan = BookLoan.objects.create(
                student=loan_data['student'],
                book=loan_data['book'],
                due_date=loan_data['due_date'],
                return_date=loan_data.get('return_date'),
                is_returned=loan_data.get('is_returned', False)
            )
            
            # Update book availability for active loans
            if not loan.is_returned:
                book = loan.book
                book.available_copies = max(0, book.available_copies - 1)
                book.save()
            
            status = "returned" if loan.is_returned else "overdue" if loan.due_date < now else "active"
            print(f"✅ Created {status} loan: {loan.student.name} - {loan.book.title}")
    
    print("\n🎉 Sample data creation completed!")
    print(f"📊 Created {len(students)} students, {len(books)} books, and {len(all_loans)} book loans")
    print("\n📚 You can now test the admin panel with this sample data.")


if __name__ == '__main__':
    create_sample_data()
