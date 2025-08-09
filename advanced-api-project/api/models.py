from django.db import models

# Author model: Stores details about authors.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name


# Book model: Represents a book linked to an author.
# Each book has a title, publication year, and a relationship to an Author.
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books'
    )  # One author can have many books

    def __str__(self):
        return self.title
