from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Title')
    content = models.TextField(blank=False, verbose_name='content')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created = models.DateTimeField('created', auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['topic', 'title']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user_name} on {self.article}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
