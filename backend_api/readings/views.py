from django.shortcuts import render
from rest_framework import viewsets
from .models import books
from .serializers import booksSerializer
    
class BooksViewSet(viewsets.ModelViewSet):
    queryset = books.objects.all()
    serializer_class = booksSerializer