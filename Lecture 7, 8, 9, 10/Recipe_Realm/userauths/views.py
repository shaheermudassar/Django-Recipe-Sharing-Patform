from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from userauths.models import Profile

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username = username)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Wrong Password")
        except:
            messages.error(request, f"{username} doesn't exist")
    return render(request, "login.html")

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        profile_image = request.FILES.get("profile_image")
        bio = request.POST.get("bio")
        if User.objects.filter(username = username).exists():
            messages.error(request, "username already exists")
        else:
            new_user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username=username,
                password=password,
            )
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                Profile.objects.create(
                    user = new_user,
                    profile_image = profile_image,
                    bio = bio
                )
                return redirect("home")

    return render(request, "signup.html")

def logout_view(request):
    logout(request)
    return redirect("home")