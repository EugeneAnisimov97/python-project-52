from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from task_manager.users.models import User
from task_manager.users.forms import UserForm
from django.contrib import messages


# Create your views here.
class UsersIndex(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users/users.html', {'users': users})


class UserFormCreate(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('login')
        return render(request, 'users/create.html', {'form': form})


class UserFormUpdate(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(User, id=user_id)
        if user != request.user:
            messages.error(
                request,
                'У вас нет прав для изменения другого пользователя.'
            )
            return redirect('users_index')
        form = UserForm(instance=user)
        return render(
            request,
            'users/update.html',
            {'form': form, 'user_id': user_id}
        )

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(User, id=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Пользователь успешно изменен')
            return redirect('users_index')
        return render(
            request,
            'users/update.html',
            {'form': form, 'user_id': user_id}
        )


class UserFormDelete(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(User, id=user_id)
        return render(request, 'users/delete.html', context={'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
            messages.success(request, 'Пользователь успешно удален')
        return redirect('users_index')
