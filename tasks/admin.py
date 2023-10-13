# from django.contrib import admin
# from .models import TaskModel

# admin.site.register(TaskModel)


from django.contrib import admin
from .models import TaskModel

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'priority', 'is_complete', 'created_at')

admin.site.register(TaskModel, TaskModelAdmin)
