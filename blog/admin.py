from django.contrib import admin
from blog.models import Author, Article

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)