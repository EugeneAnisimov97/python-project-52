from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.UsersIndex.as_view(), name='users_index'),
    path('create/', views.UserCreate.as_view(), name='users_create'),
    path('<int:id>/update/', views.UserFormUpdate.as_view(), name='users_update'),
    path('<int:id>/delete/', views.UserFormDelete.as_view(), name='users_delete'),
]
