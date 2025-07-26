from django import forms
from .models import Book 

class BookSearchForm(forms.Form):
    title = forms.CharField(required=False, max_length=100)

class ExampleForm(forms.ModelForm):
    """
    A sample form for creating or editing a Book.
    This can be used in templates like form_example.html.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date'] 