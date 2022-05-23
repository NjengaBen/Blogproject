from email.message import Message
import imp
import django
from django.contrib import admin
from .models import User, Blog, Message, Column

# Register your models here
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Message)
admin.site.register(Column)