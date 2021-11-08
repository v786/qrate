from django.db import models
from django.db.models.deletion import SET_DEFAULT

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=80)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Resume(models.Model):
    file = models.FileField(upload_to='storage/')
    name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now=True)
    profile = models.ForeignKey(Profile, related_name='resume', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ", " + str(self.created_at)