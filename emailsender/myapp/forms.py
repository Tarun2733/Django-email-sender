from django import forms
from .models import EmailModel

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailModel
        fields = ['to_email','subject','message']
        