from bookshelf.models import Book

Create a Book

# Create a book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

print(book)
# Output:
# <Book: 1984 by George Orwell (1949)>


# Retrieve the created book
book = Book.objects.get(title="1984")

print(book.title)
print(book.author)
print(book.publication_year)

# Output:
# 1984
# George Orwell
# 1949

# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)

# Output:
# Nineteen Eighty-Four

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())

# Output:
# <QuerySet []>
yaml
Copy
Edit
