from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Tasks
from .forms import *
# Create your views here.

class AllTasks(ListView):
    model = Tasks
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Tasks

class TaskCreate(CreateView):
    # model = Tasks
    # fields = '__all__'
    form_class = CreateForm
    template_name = 'todolist/tasks_form.html'
    success_url = reverse_lazy('home')

class TaskUpdate(UpdateView):
    # form_class = UpdateForm
    # template_name = 'todolist/tasks_update.html'
    # success_url = reverse_lazy('home')
    model = Tasks
    fields = '__all__'
    template_name = 'todolist/tasks_update.html'

class TaskDelete(DeleteView):
    # form_class = UpdateForm
    # template_name = 'todolist/tasks_update.html'
    # success_url = reverse_lazy('home')
    model = Tasks
    success_url = reverse_lazy('home')

class CurrentTasks(ListView):
    model = Tasks
    context_object_name = 'tasks'
    def get_queryset(self):
        return Tasks.objects.filter(is_finished=False)

class CompletedTasks(ListView):
    model = Tasks
    context_object_name = 'tasks'

    def get_queryset(self):
        return Tasks.objects.filter(is_finished=True)