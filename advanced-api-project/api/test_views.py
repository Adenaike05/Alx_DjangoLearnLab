from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Create sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            description="A sample description",
            published_year=2023
        )

        self.list_url = reverse("book-list")  # Ensure your DRF router uses `book-list`
        self.detail_url = reverse("book-detail", args=[self.book.id])

    def test_create_book(self):
        """Test that an authenticated user can create a book"""
        data = {
            "title": "New Book",
            "author": "Jane Smith",
            "description": "A new book description",
            "published_year": 2024
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_list_books(self):
        """Test listing all books"""
        response = self.client.get(self.list_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_book(self):
        """Test updating a book"""
        data = {
            "title": "Updated Book",
            "author": "John Doe",
            "description": "Updated description",
            "published_year": 2025
        }
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_permissions_for_unauthenticated_user(self):
        """Test that unauthenticated users cannot create books"""
        self.client.logout()
        data = {
            "title": "No Auth Book",
            "author": "Unknown",
            "description": "Should fail",
            "published_year": 2022
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_search_books(self):
        """Test search functionality"""
        url = f"{self.list_url}?search=Test"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Test" in book["title"] for book in response.data))

    def test_filter_books_by_year(self):
        """Test filter by published_year"""
        url = f"{self.list_url}?published_year=2023"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["published_year"] == 2023 for book in response.data))

    def test_order_books_by_title(self):
        """Test ordering by title"""
        url = f"{self.list_url}?ordering=title"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)