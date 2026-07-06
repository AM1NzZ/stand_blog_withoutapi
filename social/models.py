from django.db import models

# Create your models here.
class Social(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    icon= models.FileField(upload_to='images/social',default='images/social.png')

    def __str__(self):
        return self.title