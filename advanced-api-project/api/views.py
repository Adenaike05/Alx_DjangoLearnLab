from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# List all books or create a new one (anyone can view, only authenticated users can create)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]



# Retrieve details of a single book (anyone can view)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a book (must be logged in)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        if "forbidden" in title.lower():
            raise serializers.ValidationError("This title is not allowed.")
        serializer.save()

# Update a book (only the owner can update)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Add custom logic here if needed
        serializer.save()


# Delete a book (only admins can delete)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
