from django.db import models

# Create your models here.
class SimpleModel(models.Model):

    name= models.CharField(max_length=64)
    email=models.EmailField(unique=True)
    text= models.TextField()

    def __str__(self):
        return self.name
