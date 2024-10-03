from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from todo.models import Task

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Task'))
        
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed', 'assignees']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'assignees': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('assignees'):
            raise forms.ValidationError("A task must have at least one assignee.")
        return cleaned_data
