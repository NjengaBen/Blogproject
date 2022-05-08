from django.forms import ModelForm, forms
from django.contrib.auth.forms import UserCreationForm
from . models import Blog, User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['host', 'participants']
