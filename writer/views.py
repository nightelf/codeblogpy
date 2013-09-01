from django.http import HttpResponse
from django.template import RequestContext, loader
from blog.models import Article, get_latest_articles, get_latest_articles_json

def index(request):
    return HttpResponse('Writer Index Page')