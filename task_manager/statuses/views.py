from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from task_manager.mixins import CheckLoginMixin, ProtectDeletingMixin
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
        'button_text': _('Create'),
    }


class StatusUpdateView(SuccessMessageMixin, CheckLoginMixin, UpdateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status changed successfully')
    extra_context = {
        'head': _('Change of status'),
        'button_text': _('Change'),
    }


class StatusDeleteView(CheckLoginMixin,
                       SuccessMessageMixin,
                       ProtectDeletingMixin,
                       DeleteView):
    model = Status
    template_name = 'delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status successfully deleted')
    error_message = _(
        'Cannot delete this status because it is associated with a task.'
    )
    redirect_url = reverse_lazy('statuses_index')
    extra_context = {
        'head': _('Deleting a status'),
        'button_text': _('Yes, delete'),
    }
