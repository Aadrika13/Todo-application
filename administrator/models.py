from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Superuser(User):
    phone_no = models.CharField(max_length=10)