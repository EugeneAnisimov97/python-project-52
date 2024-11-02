from django.shortcuts import redirect
from task_manager.users.models import User
from task_manager.users.forms import CreateUserForm, UpdateUserForm
from django.views.generic import ListView
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.mixins import CheckLoginMixin, CustomPassesMixin
from django.utils.translation import gettext_lazy as _

# Create your views here.
class UsersIndexView(ListView):
    template_name = 'users/index.html'
    model = User
    extra_context = {
        'head': 'Users',
    }
    context_object_name = 'users'


class UserFormCreate(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = User
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    success_message = _('User registered successfully')
    extra_context = {
        'head': 'Registarion',
        'content': 'Sing-up',
    }


class UserFormUpdate(CustomPassesMixin, CheckLoginMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'form.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User successfully changed')
    extra_context = {
        'head': 'Change user',
        'content': 'Change',
    }
 
    def test_func(self):
        return self.get_object().id == self.request.user.id



class UserFormDelete(CustomPassesMixin,CheckLoginMixin,SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User successfully deleted')
    extra_context = {
        'head': 'Deleting a user',
        'content': 'Yes, delete',
    }
    
    def test_func(self):
        user = self.get_object()
        return self.request.user == user
    

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
