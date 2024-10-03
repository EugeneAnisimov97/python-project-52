from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from task_manager.users.models import User
from task_manager.users.forms import UserForm
from django.contrib import messages


# Create your views here.
class UsersIndex(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users/users.html', context={'users': users})

class UserCreate(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'users/create.html', {'form':form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('login')
        return render(request, 'users/create.html', {'form': form})