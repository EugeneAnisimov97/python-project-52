from django import forms
from task_manager.users.models import Users

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')