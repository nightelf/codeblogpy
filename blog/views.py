# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from blog.models import Article
from django.shortcuts import get_object_or_404
import datetime
from django.core import serializers

pagesize = 10

def index(request, page=0):

    # define indicies
    start_index = int(page) * pagesize
    end_index = start_index + pagesize
    
    latest_article_list = Article.objects.filter(published__lte=datetime.date.today()
        ).order_by('-published')[start_index:end_index]
    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'latest_article_list': latest_article_list,
    })
    return HttpResponse(template.render(context))

def index_json(request, page=0):
    
    # define indicies
    start_index = int(page) * pagesize
    end_index = start_index + pagesize
    
    latest_article_list = Article.objects.filter(published__lte=datetime.date.today()
        ).order_by('-published')[start_index:end_index]
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
