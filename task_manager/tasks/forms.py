from django import forms
from task_manager.tasks.models import Task

class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Имя', required=True)
    
    class Meta:
        model = Task
        fields = [
            'name', 'description',
            'status', 'executor'
        ]
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'executor': 'Исполнитель',
        }