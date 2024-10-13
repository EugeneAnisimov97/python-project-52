from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from task_manager.mixins import CheckLoginMixin
from django.contrib.auth.mixins import UserPassesTestMixin


class StatusesIndex(ListView):
    template_name = 'statuses/index.html'
    model = Status
    extra_context = {
        'head': 'Statuses',
    }
    context_object_name = 'statuses'


class StatusFormCreate(SuccessMessageMixin, CheckLoginMixin, CreateView):
    template_name = 'statuses/create.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно создан'
    extra_context = {
        'head': 'Create Status',
        'content': 'Create',
    }


class StatusFormUpdate(SuccessMessageMixin, CheckLoginMixin, UpdateView):
    template_name = 'statuses/update.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно изменен'
    extra_context = {
        'head': 'Change of status',
        'content': 'Change',
    }


class StatusFormDelete(CheckLoginMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно удален'
    extra_context = {
        'head': 'Deleting a status',
        'content': 'Yes, delete',
    }
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    