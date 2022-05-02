from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
