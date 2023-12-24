from django import forms
from .models import Blogpost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'content']
