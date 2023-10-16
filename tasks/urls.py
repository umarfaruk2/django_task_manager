from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task', views.TaskView, basename='task')

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('add_task/', views.AddTask.as_view(), name='add_task'),
    path('task_detail/<int:pk>', views.TaskDetail.as_view(), name='task_detail'), 
    path('update_task/<int:pk>', views.UpdateTask.as_view(), name='update_task'), 
    path('task_delete/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
    path('delete_current_image/<int:id>', views.delete_current_image, name='delete_current_image'),
    path('delete_image/<int:id>/<int:task_id>', views.delete_image, name='delete_image'),
    path('is_complete/<int:id>', views.is_complete, name='is_complete'),
    path('signup/', views.user_register, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    path('', include(router.urls))    
]
