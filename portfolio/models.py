from django.db import models

# Create your models here.
class Name(models.Model):
#    question_text = models.CharField(max_length=200)
    College = models.CharField(max_length=250)
    Photo = models.CharField(max_length=1000)
    Email = models.CharField(max_length=250)
    phone = models.IntegerField()
    linkedin = models.URLField(max_length=100)
    github = models.URLField(max_length=100)
