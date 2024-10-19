from django import forms
from task_manager.users.models import User
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

class UpdateUserForm(CreateUserForm):
    def clean_username(self):
        return self.cleaned_data.get('username')