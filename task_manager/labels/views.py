from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from django.urls import reverse_lazy
from task_manager.mixins import CheckLoginMixin, ProtectDeletingMixin
from django.utils.translation import gettext_lazy as _


class LabelIndex(CheckLoginMixin, ListView):
    template_name = 'labels/index.html'
    model = Label
    extra_context = {
        'head': _('Labels'),
    }
    context_object_name = 'labels'


class LabelCreateView(SuccessMessageMixin, CheckLoginMixin, CreateView):
    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels_index')
    success_message = _('Label successfully created')
    extra_context = {
        'head': _('Create Label'),
        'button_text': _('Create'),
    }


class LabelUpdateView(SuccessMessageMixin, CheckLoginMixin, UpdateView):
    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels_index')
    success_message = _('Label changed successfully')
    extra_context = {
        'head': _('Change of label'),
        'button_text': _('Change'),
    }


class LabelDeleteView(CheckLoginMixin,
                      SuccessMessageMixin,
                      ProtectDeletingMixin,
                      DeleteView):
    model = Label
    template_name = 'delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Label successfully deleted')
    error_message = _(
        'Cannot delete this label because it is associated with a task.'
    )
    redirect_url = reverse_lazy('labels_index')
    extra_context = {
        'head': _('Deleting a label'),
        'button_text': _('Yes, delete'),
    }
