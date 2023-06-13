from django import forms
from .models import *


class UserPostForm(forms.ModelForm):
    post_image = forms.ImageField(label='', required=True)
    post_content = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'placeholder': "what's on your mind ?"}))

    class Meta:
        model = Post
        fields = ['post_image', 'post_content']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'placeholder': 'Write Your Comment', 'rows': '5', 'cols': '2', 'style': 'resize:none'}))

    class Meta:
        model = Comment
        fields = ['comment']
