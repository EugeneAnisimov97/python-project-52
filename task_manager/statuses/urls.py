from django.urls import path
from task_manager.statuses import views


urlpatterns = [
    path('', views.StatusesIndex.as_view(), name='statuses_index'),
    path('create/', views.StatusFormCreate.as_view(), name='statuses_create'),
    path('<int:pk>/update/', views.StatusFormUpdate.as_view(), name='statuses_update'),  # noqa: E501
    path('<int:pk>/delete/', views.StatusFormDelete.as_view(), name='statuses_delete'),  # noqa: E501
]
