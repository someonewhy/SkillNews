from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')
