from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView
)
from django.urls import reverse_lazy
from task_manager.mixins import CheckLoginMixin
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
class TasksIndex(CheckLoginMixin, ListView):
    template_name = 'tasks/index.html'
    model = Task
    extra_context = {
        'head': 'Tasks',
    }
    context_object_name = 'tasks'


class TaskCreateView(SuccessMessageMixin, CheckLoginMixin, CreateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_index')
    success_message = 'Задача успешно создана'
    extra_context = {
        'head': 'Create task',
        'content': 'Create',
    }
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(SuccessMessageMixin, CheckLoginMixin, UpdateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_index')
    success_message = 'Задача успешно изменена'
    extra_context = {
        'head': 'Change task',
        'content': 'Change',
    }
class TaskDeleteView(CheckLoginMixin, SuccessMessageMixin, DeleteView):
    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks_index')
    success_message = 'Задача успешно удалена'
    extra_context = {
        'head': 'Delete task',
        'content': 'Yes, delete',
    }
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            messages.error(request, "Задачу может удалить только ее автор")
            return redirect('tasks_index')
        return super().dispatch(request, *args, **kwargs)
class TaskDetailView(CheckLoginMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'