from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.


def home(request):
    return render(request, 'index.html', {'title': 'Home'})


def profile(request, pk):
    profile = User.objects.get(id=pk)
    return render(request, 'profile.html', {'title': 'Profile', 'profile': profile})


def edit_profile(request):

    user = request.user
    # Test if profile is created
    try:
        # If profile is created, get the profile
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # If profile is not created, create a new profile
        profile = Profile(user=user)
        profile.save_user()

    if request.method == 'POST':
        bio = request.POST['bio_info']

        # check if profile pic is uploaded to update if not use the default or the old one
        try:
            file = request.FILES['profile_pic']
        except:
            file = profile.profile_pic

        # Test if profile is created
        profile = Profile.objects.get(user=user)
        profile.bio = bio
        profile.profile_pic = file
        profile.save()

    return render(request, 'edit_profile.html', {'title': 'Edit Profile', 'profile': profile})


def submit_project(request):
    return render(request, 'submit_project.html', {'title': 'Submit Project'})
