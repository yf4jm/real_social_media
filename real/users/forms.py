from django import forms
from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm
from posts.models import Badge

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','username', 'email','password1', 'password2']
    def save(self, commit=True):
            user = super().save(commit=False)
            user.username = user.username.lower()
            
            if commit:
                user.save()
                badge=Badge.objects.get(id=1)
                # Create a profile associated with the user
                Profile.objects.create(user=user,name=user.first_name, username=user.username.lower(),badge=badge, email=user.email)

            return user




