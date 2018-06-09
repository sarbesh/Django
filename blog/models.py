from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
        .filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default = 'Draft')
    #object = models.Manager #Default manager
    published = PublishedManager() #custom manager
    
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        #return reverse('blog:post_details',args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'),self.slug])
        return reverse('post_details',args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'),self.slug])
        #for app_name = "blog in urls.py the app will be registered as blog which can be used in reverse('blog:____')" :- this is registering the app
