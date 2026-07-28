from django.contrib.auth.models import User ,AbstractBaseUser
from django.db import models 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/image',blank=True,null=True)

    class Meta:
        verbose_name = "Profile"
        
    def __str__(self):
        return self.user.username