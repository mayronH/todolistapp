"""Forms"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    """Signup Form"""
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserForm(forms.ModelForm):
    """Default User Form"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': "Nome:",
            'last_name': "Sobrenome:",
            'email': "E-mail:",
        }

class ProfileForm(forms.ModelForm):
    """User Profile Form"""
    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio')
        labels = {
            'profile_pic': "Avatar:",
            'bio': "Biografia:",
        }
