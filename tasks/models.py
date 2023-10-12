from django.db import models

class AddTaskModel(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=200, default=None)
    due_date = models.DateTimeField(default=None)
    barth_date = models.DateTimeField(default=None)