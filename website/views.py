from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
def home_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you logged in successfully...")
            return redirect("website:home")
        else:
            messages.error(request, "username or password was incorrect!!!")
            return redirect("website:home")
    return render(request, "home.html", {})


def logout_view(request):
    logout(request)
    messages.info(request, "YOU'VE LOGGED OUT...")
    return redirect("website:home")