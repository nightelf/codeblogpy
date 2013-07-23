# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from blog.models import Article
from django.shortcuts import get_object_or_404
import datetime

def index(request):
    latest_article_list = Article.objects.filter(published__lte=datetime.date.today()
        ).order_by('-published')[:10]
    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'latest_article_list': latest_article_list,
    })
    return HttpResponse(template.render(context))

def articles(request, article_title):
    my_article = get_object_or_404(
        Article, slug=article_title, published__lte=datetime.date.today()
    )
    authors = my_article.authors.all()
    template = loader.get_template('blog/article.html')
    context = RequestContext(request, {
        'article' : my_article,
        'authors' : authors
    })
    return HttpResponse(template.render(context))
