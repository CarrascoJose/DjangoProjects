from django.shortcuts import render
from django.views.generic import ListView
from .models import AppUser

# Create your views here.

class HomePageView(ListView):
    model = AppUser
    template_name = 'notes/home.html'

    def get_queryset(self):
        return self.model.objects.all()