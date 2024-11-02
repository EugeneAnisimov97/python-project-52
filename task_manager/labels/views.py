from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from django.shortcuts import redirect
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from django.urls import reverse_lazy
from task_manager.mixins import CheckLoginMixin, ProtectDeletingMixin
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import TasksRelationLabels
from django.contrib import messages
from django.db.models import ProtectedError

# Create your views here.
class LabelIndex(CheckLoginMixin, ListView):
    template_name = 'labels/index.html'
    model = Label
    extra_context = {
        'head': 'Labels',
    }
    context_object_name = 'labels'


class LabelCreateView(SuccessMessageMixin, CheckLoginMixin, CreateView):
    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels_index')
    success_message = _('Label successfully created')
    extra_context = {
        'head': 'Create Label',
        'content': 'Create',
    }


class LabelUpdateView(SuccessMessageMixin, CheckLoginMixin, UpdateView):
    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels_index')
    success_message = _('Label changed successfully')
    extra_context = {
        'head': 'Change of label',
        'content': 'Change',
    }


class LabelDeleteView(CheckLoginMixin, SuccessMessageMixin, ProtectDeletingMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Label successfully deleted')
    error_message = _('Cannot delete this label because it is associated with a task.')
    redirect_url = 'labels_index'
    extra_context = {
        'head': 'Deleting a label',
        'content': 'Yes, delete',
    }


    # def delete(self, request, *args, **kwargs):
    #     label = self.get_object()
    #     if TasksRelationLabels.objects.filter(label=label).exists():
    #         messages.error(request, _('Cannot delete this label because it is associated with a task.'))
    #         return redirect('labels_index')
    #     return super().delete(request, *args, **kwargs)