from django.db import models

# Create your models here.

class Todo(models.Model):
    title =  models.CharField(("Title"), max_length=200)
    completed = models.BooleanField()
    date_added = models.DateTimeField(('date added'), auto_now_add=True)
    date_updated = models.DateTimeField(('date updated'), auto_now=True)


    def __str__(self):
        return self.title