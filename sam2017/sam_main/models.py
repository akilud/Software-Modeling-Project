from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='UserProfile')
    is_admin = models.BooleanField(default=0)
    is_pcc = models.BooleanField(default=0)
    is_pcm = models.BooleanField(default=0)
    is_author = models.BooleanField(default=1)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
