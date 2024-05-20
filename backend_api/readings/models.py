from django.db import models

# Create your models here.
class books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    genre = models.CharField(max_length=100)
    published_year = models.IntegerField()
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=255)
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    description = models.TextField()
    cover_image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title + ' - ' + self.author 