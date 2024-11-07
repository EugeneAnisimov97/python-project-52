from django import forms
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _

class TaskForm(forms.ModelForm):  
    class Meta:
        model = Task
        fields = [
            'name', 'description',
            'status', 'executor', 'labels'
        ]
        widgets = {
            'labels': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-control',
                'style': 'max-height: 150px; overflow-y: auto;'
                })
        }