from django import forms
from task_manager.users.models import Users
import re

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = ''
        self.fields['last_name'].initial = ''
        self.fields['username'].initial = ''
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and len(password1) < 3:
            self.add_error('password1', "Введённый пароль слишком короткий. Он должен содержать как минимум 3 символа.")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Пароли не совпадают.")
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match(r'^[\wа-яА-ЯёЁ@._+-]+$', username):
            raise forms.ValidationError("Введите правильное имя пользователя. Оно может содержать только буквы (латиница и кириллица), цифры и знаки @/./+/-/_.")

        if Users.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует.")
        return username
    