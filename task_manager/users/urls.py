from django.urls import path
from task_manager.users import views


urlpatterns = [
    # BEGIN (write your solution here)
    path('', views.UsersIndex.as_view(), name='users_index'),
    # END
]
