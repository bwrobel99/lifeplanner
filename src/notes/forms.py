from django import forms
from .models import Note, Todo
import datetime

class NoteCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoteCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs.update(placeholder="give it a nice, unique title")
        self.fields['body'].widget.attrs.update(rows='3', placeholder="what do you want to remember?")

    class Meta:
        model = Note
        fields = [
            'title', 
            'body', 
        ]


class TodoCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TodoCreateForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Todo
        fields = [
            'body',
            'deadline'
        ]
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control'
                
            }),
            'deadline': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            })
        }
