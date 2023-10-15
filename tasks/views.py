from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import TaskModelForm
from .models import TaskModel, TaskImageModel
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import DetailView, DeleteView, ListView
from django.forms import modelformset_factory

# class Home(ListView):
#     model = TaskModel
#     template_name = 'task/home.html'
#     context_object_name = 'tasks'
    
#     def get_queryset(self):
#         search_value = self.request.GET.get('search')
#         search_by_due = self.request.GET.get('search_by_due')
#         search_by_creation = self.request.GET.get('search_by_creation')
#         search_by_priority = self.request.GET.get('priority') 
#         search_by_status = self.request.GET.get('status') 

#         if search_value:
#             queryset = TaskModel.objects.filter(user = self.request.user, title__icontains = search_value)
#         else:
#             queryset = TaskModel.objects.filter(user = self.request.user)
        
#         if search_by_creation:
#             queryset = TaskModel.objects.filter(user = self.request.user, created_at__date = search_by_creation)

#         if search_by_due:
#             queryset = TaskModel.objects.filter(user = self.request.user, due_date = search_by_due)
        
#         if search_by_priority:
#             queryset = TaskModel.objects.filter(user = self.request.user, priority = search_by_priority)
        
#         if search_by_status:
#             if search_by_status == 'complete':
#                 queryset = TaskModel.objects.filter(user = self.request.user, is_complete = True)
#             else:
#                 queryset = TaskModel.objects.filter(user = self.request.user, is_complete = False)
        
#         queryset = queryset.order_by('priority')  

#         return queryset
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['task_images'] = TaskImageModel.objects.all()
#         return context

class Home(ListView):
    model = TaskModel
    template_name = 'task/home.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        search_value = self.request.GET.get('search')
        search_by_due = self.request.GET.get('search_by_due')
        search_by_creation = self.request.GET.get('search_by_creation')
        search_by_priority = self.request.GET.get('priority') 
        search_by_status = self.request.GET.get('status') 

        if search_value:
            queryset = TaskModel.objects.filter(user = self.request.user, title__icontains = search_value)
        else:
            queryset = TaskModel.objects.filter(user = self.request.user)
        
        if search_by_creation:
            queryset = TaskModel.objects.filter(user = self.request.user, created_at__date = search_by_creation)

        if search_by_due:
            queryset = TaskModel.objects.filter(user = self.request.user, due_date = search_by_due)
        
        if search_by_priority:
            queryset = TaskModel.objects.filter(user = self.request.user, priority = search_by_priority)
        
        if search_by_status:
            if search_by_status == 'complete':
                queryset = TaskModel.objects.filter(user = self.request.user, is_complete = True)
            else:
                queryset = TaskModel.objects.filter(user = self.request.user, is_complete = False)
        
        # queryset = queryset.order_by('priority')  
        
        def custom_priority_sort(task):
            priority_order = {
                'High': 0,
                'Medium': 1,
                'Low': 2,
            }
            return priority_order.get(task.priority, 3)

        queryset = sorted(queryset, key=custom_priority_sort)

        for task in queryset:
            task.image = TaskImageModel.objects.filter(task=task).first()
            
        return queryset


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     tasks_with_images = []
    #     for task in context['tasks']:
    #         task_images = TaskImageModel.objects.filter(task=task)
    #         print(task_images)
    #         tasks_with_images.append({
    #             'task': task,
    #             'images': task_images,
    #         })
    #     context['tasks_with_images'] = tasks_with_images
    #     return context 

# add task
# class AddTask(FormView):
#     template_name = 'task/add_task.html'
#     form_class = TaskModelForm
    

#     def form_valid(self, form):
#         task = form.save(commit=False)
#         task.user = self.request.user

#         # Save the images
#         if 'image' in self.request.FILES:
#             images = self.request.FILES.getlist('image')
#             print(images)
#             for image in images:
#                 task.image = image 
#                 task.save()
#         else:
#             print('not have any image')
# #         # Save the task
# #         task.save()
            
#         return redirect('home')

class AddTask(FormView):
    template_name = 'task/add_task.html'
    form_class = TaskModelForm  

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()

        # Save the images
        for image in form.cleaned_data['image']:
            task_image = TaskImageModel(task=task, image=image)  
            task_image.save()

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

# is_compete
def is_complete(request, id):
    task = TaskModel.objects.get(pk = id) 
    if task.is_complete:
        task.is_complete = False
    else:
        task.is_complete = True
    task.save()

    return redirect('task_detail', pk = id)

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