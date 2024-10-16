# from task_manager.forms import LoginForm
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    next_page = reverse_lazy('index')
    success_message = "Вы залогинены"
    extra_context = {
        'head': 'Log In',
        'content': 'Log In',
    }


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогигены')
        return super().dispatch(request, *args, **kwargs)
