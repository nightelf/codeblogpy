from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mobile.views.index', name='home'),
    url(r'^(\d{1,3})$', 'mobile.views.index', name='index'),
    url(r'^article/([.\w+-]+)$', 'mobile.views.article', name='article'),
    url(r'^navigation/', 'mobile.views.nav', name='nav'),
    url(r'^contact/', 'mobile.views.contact', name='contact'),
    url(r'^json/(\d{1,3})$', 'mobile.views.index_json', name='index_json')
    
    # Examples:
    # url(r'^$', 'news_blog.views.home', name='home'),
    # url(r'^news_blog/', include('news_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
