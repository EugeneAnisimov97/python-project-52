from django import forms
from task_manager.statuses.models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Имя', required=True)

    class Meta:
        model = Status
        fields = ['name']
