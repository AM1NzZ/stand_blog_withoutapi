from contextlib import nullcontext
from email.policy import default

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.

#DataBase Atrri
# cascade
# set null

# protect
# set default
class Category(models.Model):
    title = models.CharField(max_length=100,help_text='Enter your title')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(published=True)

class Article(models.Model):
    CHOICES = (
        ('Hola','Hola'),
        ('NoaH','NoaH'),
        ('Casa','Casa'),
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,help_text='Enter your title')
    category = models.ManyToManyField(Category,related_name='articles')
    body = RichTextField()
    image = models.ImageField(upload_to = 'images/article')
    postimage = models.ImageField(upload_to='images/article',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    myfile = models.FileField(upload_to = 'files/article',null=True,blank=True)
    objects = ArticleManager()

    def __str__(self):
        return f'{self.author} - {self.title} '


