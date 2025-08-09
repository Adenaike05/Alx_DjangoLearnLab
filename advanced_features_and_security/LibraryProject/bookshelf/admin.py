from django.contrib import admin
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import HttpResponse


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "date_of_birth", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


@permission_required("bookshelf.can_view", raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, "bookshelf/article_list.html", {"articles": articles})


@permission_required("bookshelf.can_create", raise_exception=True)
def article_create(request):
    return HttpResponse("Create Article View (Only for Editors and Admins)")


@permission_required("bookshelf.can_edit", raise_exception=True)
def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return HttpResponse(f"Edit Article: {article.title}")


@permission_required("bookshelf.can_delete", raise_exception=True)
def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return HttpResponse(f"Delete Article: {article.title}")
