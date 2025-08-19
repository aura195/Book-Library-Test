"""
URL configuration for core app.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookLoanAdminViewSet, StudentViewSet, BookViewSet

router = DefaultRouter()
router.register(r'book-loans', BookLoanAdminViewSet, basename='bookloan')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
