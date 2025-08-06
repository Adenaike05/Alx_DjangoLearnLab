from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer: Serializes all fields of the Book model.
# Includes validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer: Serializes the Author model with a nested BookSerializer.
# This allows each author instance to show a list of their books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']