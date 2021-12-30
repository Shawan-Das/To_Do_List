from django.db import models
from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name='tasks'

#Show Task Details
class TaskDetail(DetailView):
    model = Task #model name
    context_object_name= 'task' #object name
    template_name= 'base/task.html' #template name

#create a new Task
class TaskCreate(CreateView):
    model = Task
    fields = '__all__' #will edit all
    success_url= reverse_lazy('tasks')
    template_name = 'base/form.html'

#Edit Task details
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url= reverse_lazy('tasks')
    template_name = 'base/form.html'

#delete Task
class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url= reverse_lazy('tasks')
    template_name='base/confirm_delete.html'