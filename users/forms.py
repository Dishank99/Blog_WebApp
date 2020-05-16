from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User #Specifies the model in which the form data should be saved
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]# this list specifies the sequesnce in which the fields of form should be appeared        

#form for updating user information i.e email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]

#form for updating profile picture that will use Profile model
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image'
        ]