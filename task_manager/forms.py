from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')


class LogoutForm(forms.Form):
    pass
