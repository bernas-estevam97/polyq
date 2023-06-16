from django.forms import ModelForm, TextInput, EmailInput, Textarea

from .models import Form


class FeedbackForm(ModelForm):
    class Meta:
        model = Form
        fields = ('visitor_name', 'email', 'subject', 'message')
        widgets={
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
