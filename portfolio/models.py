from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Name(models.Model):
#    question_text = models.CharField(max_length=200)
    First_name = models.CharField(max_length=100, default='')
    Middle_name = models.CharField(max_length=100, default='')
    Last_name = models.CharField(max_length=100, default='')
    Email = models.EmailField(default="", max_length=250, primary_key=True)
#    User = models.CharField(max_length=250, default='')
#    College = models.CharField(max_length=250)
    DOB = models.DateField(blank=False,default='', null =True)
    #Photo =StdImageField(upload_to='user/Image/', variations={'thumbnail': (150,200,True)})
    phone = models.IntegerField()
    linkedin = models.URLField(max_length=100, blank = True)
    github = models.URLField(max_length=100, blank = True)
