from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    is_editor = models.BooleanField()
    picture_file = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.first_name + self.last_name
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    body_html = models.TextField()
    body = models.TextField()
    authors = models.ManyToManyField(Author)
    editor = models.ForeignKey(Author, related_name='the_editor')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.DateTimeField()
    def __unicode__(self):
        return self.title
