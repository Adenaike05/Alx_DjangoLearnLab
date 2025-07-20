from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific authordef get_books_by_author(author_name):
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print(f"Books in {library.name}:", list(books_in_library))

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian of {library.name}:", librarian.name)