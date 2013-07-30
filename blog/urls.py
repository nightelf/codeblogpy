from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='home'),
    url(r'^(\d{1,3})$', 'blog.views.index', name='index'),
    url(r'^([.\w+-]+)$', 'blog.views.articles', name='articles'),
    url(r'^json/(\d{1,3})$', 'blog.views.index_json', name='index_json')
    
    # Examples:
    # url(r'^$', 'news_blog.views.home', name='home'),
    # url(r'^news_blog/', include('news_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
