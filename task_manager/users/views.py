from django.shortcuts import redirect
from task_manager.users.models import User
from task_manager.users.forms import CreateUserForm
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from task_manager.mixins import CheckLoginMixin
from django.contrib.auth import logout

# Create your views here.
class UsersIndex(ListView):
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
    success_message = 'Пользователь успешно зарегистрирован'
    extra_context = {
        'head': 'Registarion',
        'content': 'Sing-up',
    }


class UserFormUpdate(UserPassesTestMixin, CheckLoginMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = CreateUserForm
    template_name = 'form.html'
    success_url = reverse_lazy('users_index')
    success_message = 'Пользователь успешно изменен'
    extra_context = {
        'head': 'Change user',
        'content': 'Change',
    }
 
    def test_func(self):
        return self.get_object().id == self.request.user.id
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, 'У вас нет прав для изменения другого пользователя')
        else:
            return super().handle_no_permission()
        return redirect(self.success_url)



class UserFormDelete(UserPassesTestMixin,CheckLoginMixin,SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_index')
    success_message = 'Пользователь успешно удален'
    extra_context = {
        'head': 'Deleting a user',
        'content': 'Yes, delete',
    }
    
    def test_func(self):
        user = self.get_object()
        return self.request.user == user
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, 'У вас нет прав для удаления другого пользователя')
        else:
            return super().handle_no_permission()
        return redirect(self.success_url)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
