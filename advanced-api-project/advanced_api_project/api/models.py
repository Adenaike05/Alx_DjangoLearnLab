from django.db import models

# Author model: represents a writer who can have multiple books.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model: represents a book written by an author.
# Each book has a title, publication year, and a foreign key linking it to an Author.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
