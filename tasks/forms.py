from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TaskModel

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', help_text='')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Again', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'due_date', 'priority', 'image']
