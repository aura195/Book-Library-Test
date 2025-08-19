from rest_framework import serializers
from .models import BookLoan, Student, Book


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'student_id', 'created_at', 'updated_at']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_year', 'available_copies', 'created_at', 'updated_at']


class BookLoanSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    student_id = serializers.IntegerField(write_only=True)
    book = BookSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = BookLoan
        fields = [
            'id', 'student', 'student_id', 'book', 'book_id', 
            'loan_date', 'return_date', 'due_date', 'is_returned',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['loan_date', 'created_at', 'updated_at']

    def validate(self, data):
        # Only validate student_id and book_id if they are provided (for creation)
        if 'student_id' in data:
            # Check if student exists
            try:
                student = Student.objects.get(id=data['student_id'])
            except Student.DoesNotExist:
                raise serializers.ValidationError("Student not found")
        
        if 'book_id' in data:
            # Check if book exists
            try:
                book = Book.objects.get(id=data['book_id'])
            except Book.DoesNotExist:
                raise serializers.ValidationError("Book not found")
            
            # Check if book is available (if creating new loan)
            if self.instance is None:  # Creating new loan
                if book.available_copies <= 0:
                    raise serializers.ValidationError("Book is not available for loan")
        
        return data

    def create(self, validated_data):
        student_id = validated_data.pop('student_id')
        book_id = validated_data.pop('book_id')
        
        student = Student.objects.get(id=student_id)
        book = Book.objects.get(id=book_id)
        
        # Decrease available copies
        book.available_copies -= 1
        book.save()
        
        return BookLoan.objects.create(
            student=student,
            book=book,
            **validated_data
        )

    def update(self, instance, validated_data):
        # Handle book return
        if validated_data.get('is_returned') and not instance.is_returned:
            instance.return_date = validated_data.get('return_date')
            instance.is_returned = True
            
            # Increase available copies
            book = instance.book
            book.available_copies += 1
            book.save()
        
        # Update other fields using the parent method
        return super().update(instance, validated_data)
