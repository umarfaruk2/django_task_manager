from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TaskModel
from multiupload.fields import MultiFileField

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', help_text='')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Again', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class TaskModelForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Select a due date'}),
    )

    image = MultiFileField(min_num=1, max_num=20, max_file_size=1024*1024*5) 
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'due_date', 'priority', 'image']
