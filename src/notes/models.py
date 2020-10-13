from django.db import models
import datetime

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length = 50, null = True, blank = True)
    body = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)


class Todo(models.Model):
    body = models.TextField()
    isDone = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()

# todos as many-to-one SQL relationship?
