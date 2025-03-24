from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea

from .models import Form


class FeedbackForm(ModelForm):
    # Honeypot field – not saved to the database
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="Leave empty"
    )

    class Meta:
        model = Form
        fields = ('visitor_name', 'email', 'subject', 'message')  # do NOT include 'honeypot' here
        widgets = {
            'visitor_name': TextInput(attrs={
                'placeholder': 'name...',
            }),
            'email': EmailInput(attrs={
                'placeholder': 'email...',
            }),
            'subject': TextInput(attrs={
                'placeholder': 'subject...'
            }),
            'message': Textarea(attrs={
                'placeholder': 'Your message...',
                'style': 'resize:none;'
            })
        }
