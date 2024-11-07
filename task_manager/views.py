# from task_manager.forms import LoginForm
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    next_page = reverse_lazy('index')
    success_message = _("You are logged in")
    extra_context = {
        'head': _('Log In'),
        'button_text': _('Log In'),
    }


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)

def index(request):
    divisionby_zero = 1 / 0
    return HttpResponse("error")