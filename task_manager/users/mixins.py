from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect


class CheckSelfUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().id == self.request.user.id

    def handle_no_permission(self):
        message = _("You do not have permission to change")
        messages.error(self.request, message)
        return redirect('users_index')
