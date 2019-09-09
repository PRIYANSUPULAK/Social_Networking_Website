from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.

class SignUp(CreateView):
    # brackets are not used after class name because we are not initialising the class here.
    form_class = forms.UserCreateForm
    # Reverse_Lazy is called instead of reverse only because we want to be redirected to login page
    # once the signup button is clicked
    success_url = reverse_lazy("login")
    template_name = 'accounts/signup.html'
