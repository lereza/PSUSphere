from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Organization

class HomePageView(ListView):
    model = Organization          # This will display a list of Organization objects
    context_object_name = 'home'  # This will be the name used to access the list in the template context
    template_name = "home.html"   # This specifies the template to render (home.html)
