#!/usr/bin/env python3
"""
Simple API testing script that temporarily uses test ViewSets.
This script tests the API endpoints without authentication.
"""

import os
import sys
import django
import requests
import json
from datetime import datetime, timedelta

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_management.settings_test')
django.setup()

# Temporarily replace the URLs to use test ViewSets
import core.urls
original_urlpatterns = core.urls.urlpatterns

# Import test ViewSets
from core.admin_test import BookLoanAdminViewSet, StudentViewSet, BookViewSet
from rest_framework.routers import DefaultRouter

# Create test router
test_router = DefaultRouter()
test_router.register(r'book-loans', BookLoanAdminViewSet, basename='bookloan')
test_router.register(r'students', StudentViewSet, basename='student')
test_router.register(r'books', BookViewSet, basename='book')

# Replace URL patterns
core.urls.urlpatterns = [
    *test_router.urls,
]

# API base URL
BASE_URL = "http://localhost:8001/api"

def test_api_endpoints():
    """Test the main API endpoints."""
    
    print("🧪 Testing Library Management API (Test Mode)...")
    print("=" * 60)
    
    # Test 1: Get all book loans
    print("\n1. Testing GET /api/book-loans/")
    try:
        response = requests.get(f"{BASE_URL}/book-loans/")
        if response.status_code == 200:
            loans = response.json()
            print(f"✅ Success! Found {len(loans)} book loans")
            if loans:
                print(f"   Sample loan: {loans[0]['student']['name']} - {loans[0]['book']['title']}")
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 2: Get statistics
    print("\n2. Testing GET /api/book-loans/statistics/")
    try:
        response = requests.get(f"{BASE_URL}/book-loans/statistics/")
        if response.status_code == 200:
            stats = response.json()
            print(f"✅ Success! Statistics: {stats}")
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 3: Get all students
    print("\n3. Testing GET /api/students/")
    try:
        response = requests.get(f"{BASE_URL}/students/")
        if response.status_code == 200:
            students = response.json()
            print(f"✅ Success! Found {len(students)} students")
            if students:
                print(f"   Sample student: {students[0]['name']}")
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 4: Get all books
    print("\n4. Testing GET /api/books/")
    try:
        response = requests.get(f"{BASE_URL}/books/")
        if response.status_code == 200:
            books = response.json()
            print(f"✅ Success! Found {len(books)} books")
            if books:
                print(f"   Sample book: {books[0]['title']} by {books[0]['author']}")
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 5: Test filtering
    print("\n5. Testing filtering by student name")
    try:
        response = requests.get(f"{BASE_URL}/book-loans/?student_name=Alice")
        if response.status_code == 200:
            loans = response.json()
            print(f"✅ Success! Found {len(loans)} loans for Alice")
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 6: Test overdue loans
    print("\n6. Testing GET /api/book-loans/overdue_loans/")
    try:
        response = requests.get(f"{BASE_URL}/book-loans/overdue_loans/")
        if response.status_code == 200:
            overdue = response.json()
            print(f"✅ Success! Found {len(overdue)} overdue loans")
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 API testing completed!")
    
    # Restore original URL patterns
    core.urls.urlpatterns = original_urlpatterns

if __name__ == "__main__":
    test_api_endpoints()
