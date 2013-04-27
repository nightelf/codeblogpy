from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=255)
    body_html = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(Author)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)
    published = DateTimeField()
        
class Author(models.Model):
    first_name = models.Charfield(max_length=30)
    last_name = models.Charfield(max_length=40)
    picture_file = models.Charfield(max_length=40)
    created = DateTimeField(auto_now_add=True)