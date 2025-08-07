from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer

# 📘 List all books and create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow only authenticated users to create, everyone can view
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    
    def perform_create(self, serializer):
        # Example: print title before saving (optional for debugging)
        print("Creating book:", serializer.validated_data.get('title'))
        serializer.save()

# 📗 Retrieve, update, or delete a specific book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow only authenticated users to update/delete, everyone can view
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    
    def perform_update(self, serializer):
        # Example: print update info (optional for debugging)
        print("Updating book:", serializer.validated_data.get('title'))
        serializer.save()
        
# BookListCreateView:
# - GET: Public endpoint to list all books
# - POST: Requires authentication to add a new book
# - Uses custom permission logic via get_permissions()
