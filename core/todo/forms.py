from django import forms
from .models import Tasks

class TasksForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-4",
                "name": "title",
                "placeholder": "enter the title",
            }
        ),
        label="",
    )
    
    class Meta:
        model = Tasks
        fields = ['title']