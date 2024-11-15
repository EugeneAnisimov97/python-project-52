from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.urls import reverse_lazy


class CheckLoginMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            message = _("You are not logged in! Please log in.")
            messages.error(request, message)
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ProtectDeletingMixin:
    error_message = _('Something went wrong')
    redirect_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.error_message)
            return redirect(self.redirect_url)
