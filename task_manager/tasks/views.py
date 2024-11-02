from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView
)
from django.urls import reverse_lazy
from task_manager.mixins import CheckLoginMixin, CustomPassesMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

# Create your views here.
class TasksIndex(CheckLoginMixin, ListView):
    template_name = 'tasks/index.html'
    model = Task
    extra_context = {
        'head': _('Tasks'),
    }
    context_object_name = 'tasks'


class TaskCreateView(SuccessMessageMixin, CheckLoginMixin, CreateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task successfully created')
    extra_context = {
        'head': _('Create task'),
        'content': _('Create'),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(SuccessMessageMixin, CheckLoginMixin, UpdateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task successfully modified')
    extra_context = {
        'head': _('Change task'),
        'content': _('Change'),
    }

class TaskDeleteView(CheckLoginMixin, SuccessMessageMixin, DeleteView):
    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task successfully deleted')
    extra_context = {
        'head': _('Delete task'),
        'content': _('Yes, delete'),
    }

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            messages.error(request, _("A task can only be deleted by its author."))
            return redirect('tasks_index')
        return super().dispatch(request, *args, **kwargs)

class TaskDetailView(CheckLoginMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
