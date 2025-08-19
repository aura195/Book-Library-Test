#!/usr/bin/env python3
"""
Simple API testing script for the Library Management System.
This script tests the main API endpoints to ensure they're working correctly.
"""

import requests
import json
from datetime import datetime, timedelta

# API base URL
BASE_URL = "http://localhost:8000/api"

def test_api_endpoints():
    """Test the main API endpoints."""
    
    print("🧪 Testing Library Management API...")
    print("=" * 50)
    
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
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 API testing completed!")

if __name__ == "__main__":
    test_api_endpoints()
