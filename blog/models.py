from django.db import models
import json
import datetime

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    is_editor = models.BooleanField()
    picture_file = models.CharField(max_length=40, blank=True, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.full_name()
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, default='')
    summary = models.CharField(max_length=255, default='')
    body_html = models.TextField()
    body = models.TextField()
    authors = models.ManyToManyField(Author)
    editor = models.ForeignKey(Author, related_name='the_editor')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(blank=True, default=None, null=True, db_index=True)
    
    def __unicode__(self):
        return u"%s" % (self.title)
    

def get_latest_articles(page=0, pagesize=2):
    """fetch the latest articles"""
    start_index = int(page) * pagesize
    end_index = start_index + pagesize
    
    return Article.objects.filter(published__lte=datetime.date.today()
        ).order_by('-published')[start_index:end_index]
        
def get_latest_articles_json(page=0, pagesize=2):
    """fetch the latest articles in JSON format"""
    articles = []
    for article in get_latest_articles(page, pagesize):
        item = {
            'title' : article.title,
            'slug' : article.slug,
            'summary' : article.summary,
            'date' : article.published.strftime('%Y-%m-%d'),
            'time' : article.published.strftime('%I:%M %p'),
            'authors' : [authors.full_name() for authors in article.authors.all()]
        }
        articles.append(item)
    return json.dumps(articles)

