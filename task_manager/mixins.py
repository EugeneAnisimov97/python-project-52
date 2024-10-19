from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


class CheckLoginMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, 'У вас нет прав для изменения другого пользователя')
            return redirect('users_index')
        else:
            messages.error(self.request, 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect('login') 
        
        
##test_func