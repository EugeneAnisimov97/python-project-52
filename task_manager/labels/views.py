from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from django.urls import reverse_lazy
from task_manager.mixins import CheckLoginMixin
from django.utils.translation import gettext_lazy as _

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


class LabelDeleteView(CheckLoginMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Label successfully deleted')
    extra_context = {
        'head': 'Deleting a label',
        'content': 'Yes, delete',
    }
