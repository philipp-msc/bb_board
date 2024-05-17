from django import forms
from django.core.exceptions import ValidationError

from .models import Ad, Response

class AdForm(forms.ModelForm):
   class Meta:
       model = Ad
       fields = [
           'title',
           'category',
           'text',
           'upload',
       ]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']