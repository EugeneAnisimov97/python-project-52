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
    labels = django_filters.ModelMultipleChoiceFilter(
        queryset=Label.objects.all(),
        label = _('Labels'),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-control', 
            'style': 'max-height: 150px; overflow-y: auto;'
        }),
        required=False
    )
    
    self_task = django_filters.BooleanFilter(
        method='show_self_task',
        widget=forms.CheckboxInput,
        label=_('Only self tasks'),
    )
    
    def show_self_task(self, queryset, arg, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
    
    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']