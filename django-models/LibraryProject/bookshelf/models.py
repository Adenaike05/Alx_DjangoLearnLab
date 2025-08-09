from django.db import models

""""
CREATE TABLE book(
    title varchar(200)
    author varchar(100)
    
)
Django ORM - Object Relational Mapper

"""


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
