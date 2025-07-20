from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # ✅ Register using views.register
    path('register/', views.register_view, name='register'),

    # ✅ Login using class-based view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # ✅ Logout using class-based view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]