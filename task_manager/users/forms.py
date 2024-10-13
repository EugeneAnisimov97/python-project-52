from django import forms
from task_manager.users.models import User
import re
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    # password1 = forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput,
    #     required=True
    # )
    # password2 = forms.CharField(
    #     label='Подтверждение пароля',
    #     widget=forms.PasswordInput,
    #     required=True
    # )

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
    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and len(password1) < 3:
    #         self.add_error('password1', "Введённый пароль слишком короткий. Он должен содержать как минимум 3 символа.")  # noqa: E501
    #     if password1 and password2 and password1 != password2:
    #         self.add_error('password2', "Пароли не совпадают.")
    #     return password2