# from django.db import models
# from django.contrib.auth.models import User

# class TaskModel(models.Model):
#     PRIORITY_CHOICES = (
#         ('Low', 'Low'),
#         ('Medium', 'Medium'),
#         ('High', 'High'),
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     due_date = models.DateTimeField()
#     priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
#     is_complete = models.BooleanField(default=False)
#     image = models.ImageField(upload_to='images/task_image', null = True, blank = True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

#     def __str__(self):
#         return self.title


from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

class TaskImageModel(models.Model):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/task_image', null=True, blank=True)

