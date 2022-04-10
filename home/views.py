from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.


def home(request):
    return render(request, 'index.html', {'title': 'Home'})


def profile(request, pk):
    profile = User.objects.get(id=pk)
    return render(request, 'profile.html', {'title': 'Profile', 'profile': profile})
