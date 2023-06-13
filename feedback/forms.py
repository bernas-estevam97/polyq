from django import forms

from .models import Form


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Form
        exclude = []