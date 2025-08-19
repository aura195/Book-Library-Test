"""
Test settings for the Library Management System.
This allows unauthenticated access to the API for testing purposes.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from library_management.settings import *

# Allow unauthenticated access for testing
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Allow unauthenticated access
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

# Disable CSRF for API testing
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# Override the URLs to use test ViewSets
ROOT_URLCONF = 'tests.urls_test'
