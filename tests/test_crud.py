#!/usr/bin/env python3
"""
CRUD Test Script for Library Management API.
This script tests Create, Read, Update, Delete operations.
"""

import requests
import json

def test_crud_operations():
    """Test all CRUD operations."""
    
    print("🧪 Testing CRUD Operations")
    print("=" * 40)
    
    API_BASE = "http://localhost:8000/api"
    
    # Test 1: CREATE - Create a new book loan
    print("\n1. Testing CREATE operation...")
    try:
        create_data = {
            "student_id": 1,
            "book_id": 1,
            "due_date": "2024-12-25T00:00:00Z"
        }
        response = requests.post(f"{API_BASE}/book-loans/", json=create_data)
        if response.status_code == 201 or response.status_code == 200:
            created_loan = response.json()
            loan_id = created_loan['id']
            print(f"✅ Successfully created loan with ID: {loan_id}")
        else:
            print(f"❌ Failed to create loan: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Error creating loan: {e}")
        return
    
    # Test 2: READ - Get the created loan
    print("\n2. Testing READ operation...")
    try:
        response = requests.get(f"{API_BASE}/book-loans/{loan_id}/")
        if response.status_code == 200:
            loan = response.json()
            print(f"✅ Successfully retrieved loan: {loan['student']['name']} - {loan['book']['title']}")
        else:
            print(f"❌ Failed to retrieve loan: {response.status_code}")
    except Exception as e:
        print(f"❌ Error retrieving loan: {e}")
    
    # Test 3: UPDATE - Update the loan
    print("\n3. Testing UPDATE operation...")
    try:
        update_data = {
            "due_date": "2024-12-30T00:00:00Z"
        }
        response = requests.patch(f"{API_BASE}/book-loans/{loan_id}/", json=update_data)
        if response.status_code == 200:
            updated_loan = response.json()
            print(f"✅ Successfully updated loan due date to: {updated_loan['due_date']}")
        else:
            print(f"❌ Failed to update loan: {response.status_code}")
    except Exception as e:
        print(f"❌ Error updating loan: {e}")
    
    # Test 4: CUSTOM ACTION - Mark as returned
    print("\n4. Testing CUSTOM ACTION (mark as returned)...")
    try:
        response = requests.post(f"{API_BASE}/book-loans/{loan_id}/mark_as_returned/")
        if response.status_code == 200:
            returned_loan = response.json()
            print(f"✅ Successfully marked loan as returned: {returned_loan['is_returned']}")
        else:
            print(f"❌ Failed to mark as returned: {response.status_code}")
    except Exception as e:
        print(f"❌ Error marking as returned: {e}")
    
    # Test 5: DELETE - Delete the loan
    print("\n5. Testing DELETE operation...")
    try:
        response = requests.delete(f"{API_BASE}/book-loans/{loan_id}/")
        if response.status_code == 204:
            print(f"✅ Successfully deleted loan with ID: {loan_id}")
        else:
            print(f"❌ Failed to delete loan: {response.status_code}")
    except Exception as e:
        print(f"❌ Error deleting loan: {e}")
    
    print("\n" + "=" * 40)
    print("🎉 CRUD operations test completed!")

if __name__ == "__main__":
    test_crud_operations()
