from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('add_task/', views.AddTask.as_view(), name='add_task'),
    path('task_detail/<int:pk>', views.TaskDetail.as_view(), name='task_detail'), 
    path('update_task/<int:pk>', views.UpdateTask.as_view(), name='update_task'), 
    path('task_delete/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
    path('signup/', views.user_register, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]
