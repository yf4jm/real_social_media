from django import forms
from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','username', 'email','password1', 'password2']
        labels = {
            'first_name': 'name',
        }
    def save(self, commit=True):
            user = super().save(commit=False)
            user.username = user.username.lower()
            
            if commit:
                user.save()

                # Create a profile associated with the user
                Profile.objects.create(user=user,name=user.name, username=user.username.lower(), email=user.email)

            return user




