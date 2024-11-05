import django_filters
from task_manager.tasks.models import Task
from django import forms
from task_manager.labels.models import Label
from task_manager.users.models import User
from django.utils.translation import gettext_lazy as _

class TaskFilter(django_filters.FilterSet):
    
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(), 
        label = _('Executor'),
        required=False
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label = ('Labels'),
        required=False
    )
    
    your_task = django_filters.BooleanFilter(
        method='show_your_task',
        widget=forms.CheckboxInput,
        label=_('Only your tasks'),
    )
    
    def show_your_task(self, queryset, arg, value):
        if self.request.user and value:
            return queryset.filter(author=self.request.user)
        return queryset
    
    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']