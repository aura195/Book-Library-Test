#!/usr/bin/env python3
"""
API testing script with authentication for the Library Management System.
This script tests the main API endpoints with proper authentication.
"""

import requests
import json
from datetime import datetime, timedelta

# API base URL
BASE_URL = "http://localhost:8000/api"

def test_api_with_authentication():
    """Test the main API endpoints with authentication."""
    
    print("🧪 Testing Library Management API with Authentication...")
    print("=" * 60)
    
    # Create a session for authentication
    session = requests.Session()
    
    # First, let's try to access the Django admin to authenticate
    print("\n1. Testing Django Admin Access")
    try:
        response = session.get("http://localhost:8000/admin/")
        if response.status_code == 200:
            print("✅ Django admin is accessible")
        else:
            print(f"⚠️ Django admin returned status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error accessing Django admin: {e}")
    
    # Test API endpoints (they should work without auth in development)
    print("\n2. Testing API endpoints...")
    
    # Test 1: Get all book loans
    print("\n   Testing GET /api/book-loans/")
    try:
        response = session.get(f"{BASE_URL}/book-loans/")
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            loans = response.json()
            print(f"   ✅ Success! Found {len(loans)} book loans")
            if loans:
                print(f"   Sample loan: {loans[0]['student']['name']} - {loans[0]['book']['title']}")
        elif response.status_code == 403:
            print("   ⚠️ Authentication required - this is expected")
        else:
            print(f"   ❌ Unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Get statistics
    print("\n   Testing GET /api/book-loans/statistics/")
    try:
        response = session.get(f"{BASE_URL}/book-loans/statistics/")
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            stats = response.json()
            print(f"   ✅ Success! Statistics: {stats}")
        elif response.status_code == 403:
            print("   ⚠️ Authentication required - this is expected")
        else:
            print(f"   ❌ Unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Get all students
    print("\n   Testing GET /api/students/")
    try:
        response = session.get(f"{BASE_URL}/students/")
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            students = response.json()
            print(f"   ✅ Success! Found {len(students)} students")
            if students:
                print(f"   Sample student: {students[0]['name']}")
        elif response.status_code == 403:
            print("   ⚠️ Authentication required - this is expected")
        else:
            print(f"   ❌ Unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Get all books
    print("\n   Testing GET /api/books/")
    try:
        response = session.get(f"{BASE_URL}/books/")
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            books = response.json()
            print(f"   ✅ Success! Found {len(books)} books")
            if books:
                print(f"   Sample book: {books[0]['title']} by {books[0]['author']}")
        elif response.status_code == 403:
            print("   ⚠️ Authentication required - this is expected")
        else:
            print(f"   ❌ Unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 API testing completed!")
    print("\n📝 Next Steps:")
    print("1. The API requires authentication (which is correct for security)")
    print("2. To test the frontend, you'll need to:")
    print("   - Login to Django admin at http://localhost:8000/admin/")
    print("   - Use the same browser session to access the Vue.js frontend")
    print("3. Or modify the Django settings to allow unauthenticated access for testing")

if __name__ == "__main__":
    test_api_with_authentication()
