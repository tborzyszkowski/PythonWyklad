from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Article(models.Model):
    STATUS = (
        ('e', 'Edit'),
        ('p','Published')
    )

    author = models.CharField('user name', max_length=100)
    title = models.CharField('title', max_length=100)
    body = models.TextField('body')
    created_on = models.DateTimeField('create time', auto_now_add=True)
    last_modified_on = models.DateTimeField('update time', auto_now=True)
    status = models.CharField('status', max_length=1, choices=STATUS)
    likes = models.PositiveIntegerField('likes', default=0)
    dislikes = models.PositiveIntegerField('dislikes', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_on']

    def get_absolute_url(self):
        return reverse('catalog:article_detail', kwargs={'article_id', self.pk})

    def get_article_id(self):
        return self.pk

class Comment(models.Model):
    user_name = models.CharField('user name', max_length=100)
    body = models.TextField('body')
    created_on = models.DateTimeField('create time', auto_now_add=True)
    article = models.ForeignKey('article', verbose_name="article", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.body[:20]

    def get_number_of_category_items(self):
        return self.blog_category.count()

    class Meta:
        ordering = ['body']

