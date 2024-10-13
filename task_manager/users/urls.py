from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.UsersIndex.as_view(), name='users_index'),
    path('create/', views.UserFormCreate.as_view(), name='users_create'),
    path('<int:pk>/update/', views.UserFormUpdate.as_view(), name='users_update'),  # noqa: E501
    path('<int:pk>/delete/', views.UserFormDelete.as_view(), name='users_delete'),  # noqa: E501
]
