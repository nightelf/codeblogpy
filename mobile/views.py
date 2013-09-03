# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from blog.models import Article, get_latest_articles, get_latest_articles_json
from django.shortcuts import get_object_or_404
import datetime
from django.core import serializers

pageSize = 2

def index(request, page=0):

    # define indicies
    template = loader.get_template('mobile/index.html')
    context = RequestContext(request, {

        'article_list' : get_latest_articles(page, pageSize),
        'page' : page,
        'pageSize' : pageSize
    })
    #return HttpResponse(template.render(context))
    return HttpResponse(template.render(context))

def index_json(request, page=0):
    
    response = HttpResponse(get_latest_articles_json(page, pageSize))
    response['Content-Type'] = 'application/json'
    return response

def article(request, article_title):
    my_article = get_object_or_404(Article, slug=article_title, published__lte=datetime.date.today())
    authors = my_article.authors.all()
    template = loader.get_template('mobile/article.html')
    context = RequestContext(request, {
        'article' : my_article,
        'authors' : authors,
    })
    #return HttpResponse(template.render(context))
    return HttpResponse(template.render(context))

def nav(request):
    
    template = loader.get_template('mobile/navigation.html')
    return HttpResponse(template.render(RequestContext(request, {})))

def contact(request):
    
    template = loader.get_template('mobile/contact.html')
    return HttpResponse(template.render(RequestContext(request, {})))