from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    image = models.ImageField(default='no_user_photo.webp')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
