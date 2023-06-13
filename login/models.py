from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile')
    date_of_birth = models.DateField()
    gender_choice = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    gender = models.CharField(max_length=6, choices=gender_choice)
    profile_pic = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.first_name
