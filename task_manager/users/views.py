from task_manager.users.models import User
from task_manager.users.forms import CreateUserForm, UpdateUserForm
from django.views.generic import ListView
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.mixins import (
    CheckLoginMixin, ProtectDeletingMixin
)
from task_manager.users.mixins import CheckSelfUserMixin
from django.utils.translation import gettext_lazy as _


class UsersIndexView(ListView):
    template_name = 'users/index.html'
    model = User
    extra_context = {
        'head': _('Users'),
    }
    context_object_name = 'users'


class UserFormCreate(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = User
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    success_message = _('User registered successfully')
    extra_context = {
        'head': _('Sign-up'),
        'button_text': _('Register'),
    }


class UserFormUpdate(CheckLoginMixin,
                     CheckSelfUserMixin,
                     SuccessMessageMixin, UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'form.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User successfully changed')
    extra_context = {
        'head': _('Change user'),
        'button_text': _('Change'),
    }


class UserFormDelete(CheckSelfUserMixin,
                     CheckLoginMixin,
                     SuccessMessageMixin,
                     ProtectDeletingMixin, DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User successfully deleted')
    error_message = _('Cannot delete a user because it is in use')
    redirect_url = reverse_lazy('users_index')
    extra_context = {
        'head': _('Deleting a user'),
        'button_text': _('Yes, delete'),
    }
