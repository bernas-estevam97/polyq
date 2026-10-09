from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
import time

from .models import Form

class NonceReCaptchaV3(ReCaptchaV3):
    def __init__(self, attrs=None, nonce=None):
        self.nonce = nonce
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs, renderer)
        if self.nonce:
            # Inject nonce into the <script> tag
            rendered = rendered.replace(
                '<script type="text/javascript">',
                f'<script nonce="{self.nonce}" type="text/javascript">'
            )
        return rendered

class FeedbackForm(ModelForm):
    def __init__(self, *args, nonce=None, **kwargs):
        # Generate a unique honeypot field name each time the form is initialized
        self.honeypot_field_name = self.generate_honeypot_field()
        super().__init__(*args, **kwargs)

        # ✅ Now we have nonce available here
        self.fields['captcha'].widget.nonce = nonce

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
        """Honeypot field name. Must be stable: a random name per instance never matched
        the name posted back, so the honeypot check could not trigger."""
        return 'website_url'

    def is_spam(self):
        """Custom spam check, used in the view."""
        if bool(self.cleaned_data.get(self.honeypot_field_name)):
            return True

        try:
            submitted_time = float(self.cleaned_data.get('holy_time', 0))
            if time.time() - submitted_time < 2:
                return True
        except (ValueError, TypeError):
            pass

        return False

    # 🧠 Invisible reCAPTCHA v3 — use the custom widget by default (you can override it)
    captcha = ReCaptchaField(widget=NonceReCaptchaV3(attrs={'required_score': 0.85}))

    class Meta:
        model = Form
        fields = ('visitor_name', 'email', 'subject', 'message')
        widgets = {
            'visitor_name': forms.TextInput(attrs={'placeholder': 'Your name...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email (optional)'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject...'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message...', 'class': 'no-resize'})
        }

