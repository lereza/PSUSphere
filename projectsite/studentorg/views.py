# studentorg/views.py
from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Organization  # Import the Organization model

class HomePageView(ListView):
    model = Organization  # Specify the model to query
    context_object_name = 'home'  # Name of the context variable that will hold the list of organizations
    template_name = 'home.html'  # Template to render