from django.contrib import admin
from .models import books


class booksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'published_year', 'isbn', 'publisher', 'pages', 'language', 'description', 'cover_image_url', 'created_at', 'updated_at', 'deleted_at', 'status']
    search_fields = ['title', 'author', 'genre', 'published_year', 'isbn', 'publisher', 'pages', 'language', 'description', 'cover_image_url', 'created_at', 'updated_at', 'deleted_at', 'status']
    list_filter = ['title', 'author', 'genre', 'published_year', 'isbn', 'publisher', 'pages', 'language', 'description', 'cover_image_url', 'created_at', 'updated_at', 'deleted_at', 'status']
    class Meta:
        model = books

admin.site.register(books)