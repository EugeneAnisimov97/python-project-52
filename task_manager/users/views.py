from django.shortcuts import render
from django.views import View
from task_manager.users.models import Users

# Create your views here.
class UsersIndex(View):
    def get(self, request, *args, **kwargs):
        users = Users.objects.all()
        return render(request, 'users/users.html', context={'users': users})