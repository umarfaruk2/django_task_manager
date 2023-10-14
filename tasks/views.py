from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import TaskModelForm
from .models import TaskModel
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import DetailView, DeleteView, ListView

class Home(ListView):
    model = TaskModel
    template_name = 'task/home.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return TaskModel.objects.filter(user = self.request.user)

# add task
class AddTask(FormView):
    template_name = 'task/add_task.html'
    form_class = TaskModelForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('home')

# update task
class UpdateTask(UpdateView):
    model = TaskModel
    form_class = TaskModelForm
    template_name = 'task/update_task.html' 
    success_url = reverse_lazy('home')

# delete task
class DeleteTask(DeleteView):
    model = TaskModel
    template_name = 'task/delete_task.html'

    success_url = reverse_lazy('home') 

# task detail page view
class TaskDetail(DetailView):
    model = TaskModel
    template_name = 'task/task_detail.html'
    context_object_name = 'tasks'

# user register
def user_register(request):
    if request.method == 'POST':
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            fm.save() 
            return redirect('login') 
    else:
        fm = RegisterForm()
    
    return render(request, 'task/register.html', {'form': fm})

# user login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request = request, data = request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username = username, password = password)

                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            fm = AuthenticationForm()
        return render(request, 'task/login.html', {'form': fm})
    else:
        return redirect('home')

def user_logout(request):
    logout(request)

    return redirect('login')