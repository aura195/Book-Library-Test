from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny  # Allow unauthenticated access for testing
from django.utils import timezone
from library.models import BookLoan, Student, Book
from library.serializers import BookLoanSerializer, StudentSerializer, BookSerializer


class BookLoanAdminViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing BookLoan objects via API.
    Replaces the classic Django admin interface.
    TEST VERSION - Allows unauthenticated access.
    """
    queryset = BookLoan.objects.all().select_related('student', 'book')
    serializer_class = BookLoanSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated access for testing
    
    def get_queryset(self):
        queryset = BookLoan.objects.all().select_related('student', 'book')
        
        # Filter by student name
        student_name = self.request.query_params.get('student_name', None)
        if student_name:
            queryset = queryset.filter(student__name__icontains=student_name)
        
        # Filter by book title
        book_title = self.request.query_params.get('book_title', None)
        if book_title:
            queryset = queryset.filter(book__title__icontains=book_title)
        
        # Filter by loan date range
        loan_date_from = self.request.query_params.get('loan_date_from', None)
        if loan_date_from:
            queryset = queryset.filter(loan_date__gte=loan_date_from)
        
        loan_date_to = self.request.query_params.get('loan_date_to', None)
        if loan_date_to:
            queryset = queryset.filter(loan_date__lte=loan_date_to)
        
        # Filter by return status
        is_returned = self.request.query_params.get('is_returned', None)
        if is_returned is not None:
            queryset = queryset.filter(is_returned=is_returned.lower() == 'true')
        
        return queryset.order_by('-loan_date')
    
    @action(detail=True, methods=['post'])
    def mark_as_returned(self, request, pk=None):
        """Custom action to mark a book as returned."""
        book_loan = self.get_object()
        
        if book_loan.is_returned:
            return Response(
                {'error': 'Book is already marked as returned'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        book_loan.is_returned = True
        book_loan.return_date = timezone.now()
        book_loan.save()
        
        # Increase available copies
        book = book_loan.book
        book.available_copies += 1
        book.save()
        
        serializer = self.get_serializer(book_loan)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def overdue_loans(self, request):
        """Get all overdue loans."""
        overdue_loans = self.get_queryset().filter(
            due_date__lt=timezone.now(),
            is_returned=False
        )
        serializer = self.get_serializer(overdue_loans, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def active_loans(self, request):
        """Get all active (non-returned) loans."""
        active_loans = self.get_queryset().filter(is_returned=False)
        serializer = self.get_serializer(active_loans, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get loan statistics."""
        total_loans = BookLoan.objects.count()
        active_loans = BookLoan.objects.filter(is_returned=False).count()
        overdue_loans = BookLoan.objects.filter(
            due_date__lt=timezone.now(),
            is_returned=False
        ).count()
        
        return Response({
            'total_loans': total_loans,
            'active_loans': active_loans,
            'overdue_loans': overdue_loans,
            'returned_loans': total_loans - active_loans
        })


class StudentViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Student objects."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated access for testing
    
    def get_queryset(self):
        queryset = Student.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset.order_by('name')


class BookViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Book objects."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated access for testing
    
    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset.order_by('title')
