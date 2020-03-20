from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Task(models.Model):

    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    remind_by = models.TimeField(default="0:0:0")


    def __str__(self):
        return self.task
