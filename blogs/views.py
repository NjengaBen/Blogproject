from distutils.log import error
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . forms import UserCreationForm
from . models import User, Blog, Message

# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
        
    context = {'page':page}
    return render(request, 'blogs/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit='false')
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    return render(request, 'blogs/login_register.html', {'form':form})

def home(request):
    context = {}
    return render(request, 'home.html', context)

def createPost(request):
    return render(request)

def update(request):
    return render(request)

def delete(request):
    return render(request)