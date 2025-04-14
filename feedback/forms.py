from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
import random
import string
import time

from .models import Form


class FeedbackForm(ModelForm):
    def __init__(self, *args, **kwargs):
        # Generate a unique honeypot field name each time the form is initialized
        self.honeypot_field_name = self.generate_honeypot_field()
        super().__init__(*args, **kwargs)

	# Add the dynamically generated honeypot field to the form fields
        self.fields[self.honeypot_field_name] = forms.CharField(
            required=False,
            widget=forms.HiddenInput,  # Use HiddenInput widget
            label="",
            initial=''  # Initial empty value for honeypot field
        )
	
        # Create a timestamp field for the time-based honeypot with a static name
        self.fields['holy_time'] = forms.CharField(
            required=False,
            widget=forms.HiddenInput,
            initial=str(time.time())  # Set current timestamp
        )

    def generate_honeypot_field(self):
        """Generate a random string for the honeypot field name."""
        return ''.join(random.choices(string.ascii_lowercase, k=10))

    def is_spam(self):
        """Custom spam check, used in the view."""
        
        # Check if the dynamically named honeypot field has been filled
        if bool(self.cleaned_data.get(self.honeypot_field_name)):  # Bot filled in the honeypot field
            return True
        
        # Time-based validation: if the form is submitted too quickly, it's likely a bot
        try:
            submitted_time = float(self.cleaned_data.get('holy_time', 0))
            current_time = time.time()
            
            # If form submission time is less than 2 seconds apart, it is considered spam
            if current_time - submitted_time < 2:
                return True
        except (ValueError, TypeError):
            # Handle cases where the timestamp is missing or invalid
            pass

        return False

    # 🧠 Invisible reCAPTCHA v3
    captcha = ReCaptchaField(widget=ReCaptchaV3(attrs={'required_score': 0.85}))

    class Meta:
        model = Form
        fields = ('visitor_name', 'email', 'subject', 'message')  # Do NOT include 'honeypot' here
        widgets = {
            'visitor_name': forms.TextInput(attrs={'placeholder': 'Your name...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email (optional)'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject...'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message...', 'style': 'resize:none;'})
        }


