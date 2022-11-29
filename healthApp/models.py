from django.db import models
from datetime import datetime, timedelta
# Create your models here.

class Client(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    def __str__(self) :
        return (self.firstName)
