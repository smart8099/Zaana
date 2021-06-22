from django.forms import ModelForm,Textarea
from django import forms
from .models import Notes



class Notes_Form(forms.ModelForm):
    class Meta:
        model = Notes
        fields=['title','note']
        widgets = {
            'note': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        