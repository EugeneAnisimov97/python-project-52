from django import forms
from task_manager.tasks.models import Task
from task_manager.labels.models import Label

class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Имя', required=True)
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )
    
    class Meta:
        model = Task
        fields = [
            'name', 'description',
            'status', 'executor', 'labels'
        ]
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'executor': 'Исполнитель',
            'labels': 'Метки'
        }