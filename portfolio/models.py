from django.db import models
import datetime
from django.utils import timezone
from stdimage import StdImageField

#class PortfolioManager(models.Manager):

# Create your models here.
class Name(models.Model):
#    question_text = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=100, default='')
    Middle_name = models.CharField(max_length=100, blank=True, null=True)
    Last_name = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100,unique=True, default='', help_text = 'Enter an custom url' )
    Email = models.EmailField(default="", max_length=250)
#    User = models.CharField(max_length=250, default='')
#    College = models.CharField(max_length=250)
    DOB = models.DateField(blank=False,default='', null =True)
    Photo = StdImageField(upload_to= 'portfolio/profile/' ,variations={'thumbnail': (150, 200, True)}, null = True, default = 'portfolio/profile/profile.png')
    phone = models.IntegerField()
    linkedin = models.URLField(max_length=100, blank = True)
    github = models.URLField(max_length=100, blank = True)

    #def __str__(self):
    #    return "{}, {}".format(self.id, self.Email)
