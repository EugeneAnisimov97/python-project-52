from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from task_manager.mixins import CheckLoginMixin
from django.utils.translation import gettext_lazy as _

class StatusesIndex(CheckLoginMixin, ListView):
    template_name = 'statuses/index.html'
    model = Status
    extra_context = {
        'head': _('Statuses'),
    }
    context_object_name = 'statuses'

class StatusCreateView(SuccessMessageMixin, CheckLoginMixin, CreateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status successfully created')
    extra_context = {
        'head': _('Create Status'),
        'content': _('Create'),
    }


class StatusUpdateView(SuccessMessageMixin, CheckLoginMixin, UpdateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status changed successfully')
    extra_context = {
        'head': _('Change of status'),
        'content': _('Change'),
    }


class StatusDeleteView(CheckLoginMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status successfully deleted')
    extra_context = {
        'head': _('Deleting a status'),
        'content': _('Yes, delete'),
    }
