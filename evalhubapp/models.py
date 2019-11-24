from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass

class Evaluator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pass

class DaycareUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pass
