# django-models/relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm  # For a basic login form

# --- Helper functions for role checks using UserProfile ---
# These functions will be used with @user_passes_test decorator.


def is_admin(user):
    """Checks if the user has the 'Admin' role."""
    # Ensure user has a userprofile and check its role
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"


def is_librarian(user):
    """Checks if the user has the 'Librarian' role."""
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"


def is_member(user):
    """Checks if the user has the 'Member' role."""
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


# --- Role-Based Views with Access Control ---


@login_required(login_url="/login/")  # Requires user to be logged in
@user_passes_test(is_admin, login_url="/login/")  # Only Admin users can access
def admin_view(request):
    """View accessible only by users with the 'Admin' role."""
    # Pass the user's role to the template context
    return render(
        request, "admin_view.html", {"user_role": request.user.userprofile.role}
    )


@login_required(login_url="/login/")
@user_passes_test(is_librarian, login_url="/login/")  # Only Librarian users can access
def librarian_view(request):
    """View accessible only by users with the 'Librarian' role."""
    return render(
        request, "librarian_view.html", {"user_role": request.user.userprofile.role}
    )


@login_required(login_url="/login/")
@user_passes_test(is_member, login_url="/login/")  # Only Member users can access
def member_view(request):
    """View accessible only by users with the 'Member' role."""
    return render(
        request, "member_view.html", {"user_role": request.user.userprofile.role}
    )


# --- General Views (Home, Login, Logout) ---


@login_required(login_url="/login/")
def home_view(request):
    """
    A general home view accessible to all logged-in users.
    Displays user's role if a UserProfile exists.
    """
    user_role = (
        request.user.userprofile.role
        if hasattr(request.user, "userprofile")
        else "None"
    )
    return render(request, "home.html", {"user_role": user_role})


def login_view(request):
    """Handles user login."""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on user's role after successful login
                if hasattr(user, "userprofile"):
                    if user.userprofile.role == "Admin":
                        return redirect("admin_panel")
                    elif user.userprofile.role == "Librarian":
                        return redirect("librarian_dashboard")
                    elif user.userprofile.role == "Member":
                        return redirect("member_dashboard")
                return redirect("home")  # Fallback if no specific role or profile
            else:
                # Invalid credentials
                return render(
                    request,
                    "login.html",
                    {"form": form, "error_message": "Invalid username or password."},
                )
    else:
        form = AuthenticationForm()  # Empty form for GET request
    return render(request, "login.html", {"form": form})


@login_required  # Requires user to be logged in to log out
def logout_view(request):
    """Handles user logout."""
    logout(request)
    return redirect("login")  # Redirect to the login page after logout
