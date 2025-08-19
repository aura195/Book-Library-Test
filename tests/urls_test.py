from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .admin_test import BookLoanAdminViewSet, StudentViewSet, BookViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'book-loans', BookLoanAdminViewSet, basename='bookloan')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'books', BookViewSet, basename='book')

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
