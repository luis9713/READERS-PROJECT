from django import serializers
from .models import books

class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = '__all__'