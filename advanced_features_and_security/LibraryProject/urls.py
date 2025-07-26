
from django.urls import path
from . import views

urlpatterns = [
    # General authentication URLs
    path('', views.home_view, name='home'), # Home page for logged-in users
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Role-based access URLs
    path('admin_panel/', views.admin_view, name='admin_panel'),
    path('librarian_dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member_dashboard/', views.member_view, name='member_dashboard'),
]

