from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class EngUser(AbstractUser):
    avatar = models.ImageField(upload_to='images/')
    birth_date = models.DateField(blank=True, null=True)

    @property
    def age(self):
        return (timezone.now() - self.birth_date).year

    def __str__(self):
        return self.username


class Words(models.Model):
    first = models.CharField(max_length=120, unique=True)
    second = models.CharField(max_length=120, unique=True)
    owner = models.ForeignKey(EngUser, on_delete=models.CASCADE)
    append_date = models.DateTimeField(auto_now_add=True)
    used_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField()
