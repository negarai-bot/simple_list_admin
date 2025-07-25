from django import forms

from .models import Postblog

class NewPostForm(forms.ModelForm):
    class Meta:
        model=Postblog
        fields = ['title','text','author','status']
