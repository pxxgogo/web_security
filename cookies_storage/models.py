from django.db import models


class Cookies_storage(models.Model):
    cookie = models.CharField(max_length=255)
    type = models.IntegerField(default=0)
# Create your models here.
