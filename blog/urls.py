from django.urls import path
from .views import ArticleList, ArticleCreate, ArticleDetail, ArticleFilter, CommentCreate

urlpatterns = [
    path('', ArticleList.as_view(), name='article-list'),
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('articles/<int:id>/', ArticleDetail.as_view(), name='article-detail'),
    path('articles/topic/<str:topic>/', ArticleFilter.as_view(), name='article-filter'),
    path(''
         '/', ArticleCreate.as_view(), name='add-article'),
    path('comments/', CommentCreate.as_view(), name='comment-create'),

]
