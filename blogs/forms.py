from django import forms
from .models import *

# blog post form
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content',)
        exclude = ('author', 'snake',)

# comment form
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment here...', 'class': 'form-control'}))
    
    class Meta:
        model = Comment
        fields = ('content',)
        exclude = ('author', 'blog_post',)