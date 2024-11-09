from django import forms
from task_manager.tasks.models import Task


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
                'style': 'max-height: 150px; overflow-y: auto;'}
            )
        }
