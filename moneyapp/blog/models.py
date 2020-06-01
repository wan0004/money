from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    instagram_username = models.CharField(max_length=50, blank=True)
    dob = models.DateField(blank=True)
    facebook_username = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    phone_no = models.IntegerField(default=0, blank=True)


    def __str__(self):
        return self.user
    




