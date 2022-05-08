from distutils.log import error
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . forms import BlogForm, UserCreationForm
from . models import Column, User, Blog, Message

# Create your views here.
def loginPage(request):
    page = 'login'
    # if request.user.is_authenticated:
    #     return redirect('home')

    # if request.method == 'POST':
    #     email = request.POST.get('email').lower
    #     password = request.POST.get('password')

    #     try:
    #         user = User.objects.get(email=email)

    #     except:
    #         messages.error(request, 'User does not exist')
        
    #     user = authenticate(request, email=email, password=password)

    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, 'Username or Password does not exist')
        
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
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'home.html', context)

def createPost(request):
    form = BlogForm()
    columns =  Column.objects.all()
    if request.method == 'POST':
        column_name = request.POST.get('column')
        column, created = Column.objects.get_or_create(name=column_name)

        Blog.objects.create(
            host = request.user,
            column = column,
            title = request.POST.get('title'),
            POST = request.POST.get('post')
        )
        return redirect('home')
    
    context = {'form':form, 'columns': columns}
    return render(request, 'blogs/blogs_form.html', context)

def update(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    columns = Column.objects.all()
    if request.method == 'POST':
        column_name = request.POST.get('column')
        column, created = Column.objects.get_or_create(name=column)        
        blog.column = column
        blog.title = request.POST.get('title')
        blog.post = request.POST.get('post')
        blog.save()
        return redirect('home')

    context = {'form': form, 'columns':columns}
    return render(request, 'blogs/blogs_form.html', context)

def delete(request, pk):
    blog = Blog.objects.all(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
   
    return render(request, 'blogs/delete.html', {'obj': blog})