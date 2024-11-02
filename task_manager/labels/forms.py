from django import forms
from task_manager.labels.models import Label


class LabelForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Имя', required=True)

    class Meta:
        model = Label
        fields = ['name']