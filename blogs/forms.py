from django import forms
from .models import *

# blog post form
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content',)
        exclude = ('author', 'snake',)