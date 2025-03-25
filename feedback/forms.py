from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea

from .models import Form


class FeedbackForm(ModelForm):
    # Honeypot field (not saved to the database)
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="Leave empty"
    )

    class Meta:
        model = Form
        fields = ('visitor_name', 'email', 'subject', 'message')  # Do NOT include 'honeypot' here
        widgets = {
            'visitor_name': TextInput(attrs={'placeholder': 'Your name...'}),
            'email': EmailInput(attrs={'placeholder': 'Email (optional)'}),
            'subject': TextInput(attrs={'placeholder': 'Subject...'}),
            'message': Textarea(attrs={'placeholder': 'Your message...', 'style': 'resize:none;'})
        }

    # Honeypot validation — if filled, block the form
    def clean_honeypot(self):
        data = self.cleaned_data.get('honeypot')
        if data:
            raise forms.ValidationError("Spam detected.")
        return data
