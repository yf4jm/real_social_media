from django import forms
from .models import Post
from users.models import Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","description","media"]


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ["username","email"]