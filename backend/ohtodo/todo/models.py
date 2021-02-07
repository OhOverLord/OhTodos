from django.db import models

class Todo(models.Model):
    completed = models.BooleanField(default=False)
    text = models.TextField()
