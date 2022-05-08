from unicodedata import name
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('create', views.createPost, name="create"),
    path('edit/<str:pk>/', views.update, name='edit'),
    path('delete/<str:pk>/', views.delete, name='delete'),  
]