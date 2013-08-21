# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from blog.models import Article, get_latest_articles, get_latest_articles_json
from django.shortcuts import get_object_or_404
import datetime
from django.core import serializers

def index(request, page=0):

    # define indicies
    latest_article_list = get_latest_articles_json(page)
    template = loader.get_template('blog/index_ng.html')
    context = RequestContext(request, {
        'latest_article_list': latest_article_list,
        'article_list_json' : get_latest_articles_json(),
        'page' : page
    })
    return HttpResponse(template.render(context))

def index_json(request, page=0):
    
    latest_article_list = get_latest_articles(page)
    data = serializers.serialize("json", latest_article_list)
    response = HttpResponse(data)
    response['Content-Type'] = 'application/json'
    return response

def articles(request, article_title):
    my_article = get_object_or_404(
        Article, slug=article_title, published__lte=datetime.date.today()
    )
    authors = my_article.authors.all()
    template = loader.get_template('blog/article.html')
    context = RequestContext(request, {
        'article' : my_article,
        'authors' : authors,
    })
    return HttpResponse(template.render(context))
