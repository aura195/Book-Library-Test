# 🧪 Test Files

This directory contains all test files for the Library Management System.

## 📁 File Structure

```
tests/
├── __init__.py
├── README.md
├── admin_test.py          # Test ViewSets with unauthenticated access
├── urls_test.py           # Test URL configuration
├── settings_test.py       # Test Django settings
├── test_api.py            # Basic API testing
├── test_api_with_auth.py  # API testing with authentication
├── test_api_simple.py     # Simple API testing script
└── quick_test.py          # Quick API verification
```

## 🚀 How to Use

### Quick Testing
```bash
# Run quick API test
python3 tests/quick_test.py

# Run with test settings
DJANGO_SETTINGS_MODULE=tests.settings_test python3 manage.py runserver 8001
```

### Manual Testing
```bash
# Test with authentication
python3 tests/test_api_with_auth.py

# Test without authentication
python3 tests/test_api_simple.py
```

## 🔧 Test Settings

The `settings_test.py` file provides:
- Unauthenticated API access
- CORS configuration for testing
- Debug mode enabled
- Test-specific URL configuration

## 📊 Expected Results

All tests should return:
- ✅ 200 status codes for API endpoints
- ✅ Correct JSON responses
- ✅ Sample data present
- ✅ Statistics working
- ✅ Filtering functional
