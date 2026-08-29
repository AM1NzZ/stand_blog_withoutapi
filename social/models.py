from django.db import models


# Create your models here.
class Social(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    icon = models.FileField(upload_to='images/social', default='images/social.png')

    def __str__(self):
        return self.title


class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.subject}"
    class Meta:
        verbose_name_plural = "Contactus"