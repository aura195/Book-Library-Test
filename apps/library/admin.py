from django.contrib import admin
from .models import Student, Book, BookLoan


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'student_id', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'student_id']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'published_year', 'available_copies']
    list_filter = ['published_year', 'created_at']
    search_fields = ['title', 'author', 'isbn']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(BookLoan)
class BookLoanAdmin(admin.ModelAdmin):
    list_display = ['student', 'book', 'loan_date', 'due_date', 'is_returned', 'return_date']
    list_filter = ['is_returned', 'loan_date', 'due_date']
    search_fields = ['student__name', 'book__title']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'loan_date'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('student', 'book')
