from django import forms
from task_manager.users.models import Users

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        if password1 and len(password1) < 3:
            raise forms.ValidationError("Ваш пароль должен содержать как минимум 3 символа.")
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Users.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует.")
        return username
    