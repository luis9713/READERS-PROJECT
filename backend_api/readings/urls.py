from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import BooksViewSet


router=DefaultRouter()

router.register('books', BooksViewSet, basename='books')

urlpatterns = [
    path('books/', views.BooksListCreateAPIView.as_view(), name='books-list-create'),
    path('books/<int:pk>/', views.BooksRetrieveUpdateDestroyAPIView.as_view(), name='books-retrieve-update-destroy'),
    
]

urlpatterns += router.urls