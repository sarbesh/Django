from django.db import models

# Create your models here.
class Name(models.Model):
#    question_text = models.CharField(max_length=200)
    First_name = models.CharField(max_length=100)
    Middle_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField(default="", max_length=250, primary_key=True)
    User = models.CharField(max_length=250)
    College = models.CharField(max_length=250)
    DOB = models.DateField('Birth date')
    #Photo =StdImageField(upload_to='user/Image/', variations={'thumbnail': (150,200,True)})
    phone = models.IntegerField()
    linkedin = models.URLField(max_length=100, blank = False)
    github = models.URLField(max_length=100, blank = False)
