from django import forms
from task_manager.users.models import User
import re
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name',
            'username', 'password1', 'password2'
        ]
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

class UpdateUserForm(UserChangeForm):
    password = None
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        required=True
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput,
        required=True
    )
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name',
            'username', 'password1', 'password2'
        ]
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
