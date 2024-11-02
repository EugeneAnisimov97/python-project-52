from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect


class CheckLoginMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            message = _("You are not logged in! Please log in.")
            messages.error(request, message)
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
        
class CustomPassesMixin(UserPassesTestMixin):
    def test_func(self):
            return self.get_object().id == self.request.user.id
        
    def handle_no_permission(self):
        message = _("You don't have permissions to modify another user.")
        messages.error(self.request, message)
        return redirect('users_index')
