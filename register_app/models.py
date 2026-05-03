from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=100)
    birth_date = models.DateField()
    image = models.ImageField(upload_to='profile_pics/image',blank=True,null=True)

    def __str__(self):
        return self.user.username