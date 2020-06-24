from django import forms
from ghostpost_app.models import GhostPost


class GhostPostForm(forms.Form):
    is_boast = forms.BooleanField(required=False)
    post = forms.CharField(max_length=280)
