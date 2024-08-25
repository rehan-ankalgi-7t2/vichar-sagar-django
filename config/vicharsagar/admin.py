from django.contrib import admin
from .models import Article, Topic, List, Comment

# Register your models here.
class ArticleCommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('articleTitle', 'author', 'publishedDate')
    inlines = [ArticleCommentInline]

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topicName',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment)
admin.site.register(List)