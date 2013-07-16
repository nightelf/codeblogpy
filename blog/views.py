# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from blog.models import Article
from django.shortcuts import get_object_or_404

def index(request):
    latest_article_list = Article.objects.order_by('-published')[:5]
    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'latest_article_list': latest_article_list,
    })
    return HttpResponse(template.render(context))

def articles(request, article_title):
    #my_article = get_object_or_404(Article, title=article_title)
    
    return HttpResponse("You're looking at aticle: '%s'." % article_title)
