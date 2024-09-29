from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.UsersIndex.as_view(), name='users_index'),
    path('create/', views.UserCreate.as_view(), name='users_create'),
]
