from django.shortcuts import render

from rest_framework import generics
from .models import books
from .serializers import booksSerializer


class BooksListCreateAPIView(generics.ListCreateAPIView):
    queryset = books.objects.all()
    serializer_class = booksSerializer


class BooksRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = books.objects.all()
    serializer_class = booksSerializer