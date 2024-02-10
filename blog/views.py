from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics

from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleCreateSerializer, CommentSerializer


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleFilter(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        topic = self.kwargs['topic']
        return Article.objects.filter(topic__name__iexact=topic)


class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'


class ArticleCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
