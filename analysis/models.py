from django.db import models

# Create your models here.
class Twittertext(models.Model):   
    text = models.TextField('Text')           
    date= models.DateTimeField('Date', auto_now=True)
    
    def __str__(self):
        return self.text