from django.db import models
from django.contrib.auth.models import User
class models_data(models.Model):
    user=models.OneToOneField(User)
    profile_pic=models.ImageField(blank=True,upload_to='profile_pics')
# Create your models here.
