from django.contrib import admin
from django.contrib.admin import register

from .models import Article, Comment, Topic


# Register your models here.
class ArticleInline(admin.TabularInline):
    model = Comment
    extra = 1


@register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'topic', 'created')
    list_display_links = ('title',)
    search_fields = ('title', 'topic__name', 'content')
    list_filter = ('topic__name', 'created')

    inlines = (ArticleInline,)


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user_name', 'content')
    list_display_links = ('article',)
    search_fields = ('article', 'user_name', 'content')
    list_filter = ('article', 'user_name',)
