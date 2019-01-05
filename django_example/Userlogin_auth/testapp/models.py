from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Aditional fields
    portfolio_site = models.URLField(blank=True)
    Profile_pic = models.ImageField(upload_to='Profile_pics', blank =True)

    def __str__(self):
        return self.user.username
