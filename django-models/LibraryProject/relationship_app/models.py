from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model
from django.db.models.signals import post_save # Import post_save signal
from django.dispatch import receiver # Import receiver decorator

# --- Existing Models (from previous task) ---
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# --- New UserProfile Model for RBAC ---
class UserProfile(models.Model):
    """
    Extends Django's built-in User model with a role field.
    Linked via a OneToOneField.
    """
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member') # Default role is 'Member'

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"

# --- Signal Handlers for Automatic UserProfile Creation ---

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a UserProfile automatically
    when a new User instance is created.
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver to save the UserProfile whenever the User instance is saved.
    This ensures the profile is always in sync.
    """
    # Check if userprofile exists before attempting to save, to prevent errors
    # during initial creation or if a user is deleted directly without cascade.
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
