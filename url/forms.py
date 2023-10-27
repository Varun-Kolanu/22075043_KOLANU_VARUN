from django import forms
from django.core.validators import URLValidator

class URLForm(forms.Form):
    long_url = forms.CharField(
        validators=[URLValidator()], 
        label="Your Long Url: ", 
        required=True, 
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        error_messages={
            'invalid': 'Enter a valid URL (e.g., https://example.com).'
        },
        )