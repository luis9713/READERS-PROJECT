from django.urls import path
from .views import BooksViewSet


urlpatterns = [
    path('books/', BooksViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('books/<int:pk>/', BooksViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),   
]
