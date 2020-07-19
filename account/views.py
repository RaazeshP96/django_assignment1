from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomUser


class SignupPageView(CreateView):
    model = CustomUser
    fields = ('username', 'password', 'first_name', 'last_name', 'email')
