#!/usr/bin/env python3
"""
Quick test script for the Library Management API.
This script tests the API endpoints to ensure they're working correctly.
"""

import requests
import json

def test_api():
    """Test the API endpoints."""
    
    print("🧪 Quick API Test")
    print("=" * 40)
    
    # Test endpoints
    endpoints = [
        ("Book Loans", "http://localhost:8001/api/book-loans/"),
        ("Students", "http://localhost:8001/api/students/"),
        ("Books", "http://localhost:8001/api/books/"),
        ("Statistics", "http://localhost:8001/api/book-loans/statistics/"),
        ("Overdue Loans", "http://localhost:8001/api/book-loans/overdue_loans/"),
    ]
    
    for name, url in endpoints:
        print(f"\nTesting {name}...")
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    print(f"✅ Success! Found {len(data)} {name.lower()}")
                elif isinstance(data, dict) and 'count' in data:
                    print(f"✅ Success! Found {data['count']} {name.lower()}")
                else:
                    print(f"✅ Success! {name}: {data}")
            else:
                print(f"❌ Failed with status {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"❌ Connection error - make sure the server is running on port 8001")
            print(f"   Run: DJANGO_SETTINGS_MODULE=tests.settings_test python3 manage.py runserver 8001")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 40)
    print("🎉 Quick test completed!")
    print("\n📝 Next steps:")
    print("1. If all tests passed, your API is working!")
    print("2. Open http://localhost:3000 to test the Vue.js frontend")
    print("3. Open http://localhost:8000 to see the Django home page")

if __name__ == "__main__":
    test_api()
