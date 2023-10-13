from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('add_task/', views.AddTask.as_view(), name='add_task'),
    path('task_detail/<int:id>', views.task_detail, name='task_detail'),
    path('signup/', views.user_register, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]
