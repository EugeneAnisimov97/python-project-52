from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView
)
from django.urls import reverse_lazy
from task_manager.mixins import CheckLoginMixin, ProtectDeletingMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.filter import TaskFilter
from django_filters.views import FilterView

# Create your views here.
class TasksIndex(CheckLoginMixin, FilterView):
    template_name = 'tasks/index.html'
    model = Task
    filterset_class = TaskFilter
    extra_context = {
        'head': _('Tasks'),
        'button_text': _('Show'),
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
        'button_text': _('Create'),
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
        'button_text': _('Change'),
    }

class TaskDeleteView(CheckLoginMixin, SuccessMessageMixin, ProtectDeletingMixin, DeleteView):
    template_name = 'delete.html'
    model = Task
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task successfully deleted')
    extra_context = {
        'head': _('Delete task'),
        'button_text': _('Yes, delete'),
    }

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            messages.error(request, _("A task can only be deleted by its author."))
            return redirect('tasks_index')
        return super().dispatch(request, *args, **kwargs)

class TaskDetailView(CheckLoginMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
