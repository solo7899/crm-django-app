from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterForm, PostForm
from .models import Record
from django.contrib.auth.models import User


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
    records = None
    if request.user.is_authenticated:
        records = (
            Record.objects.all().filter(owner=request.user).order_by("-created_at")
        )
    return render(request, "home.html", {"records": records})


def logout_view(request):
    logout(request)
    messages.info(request, "YOU'VE LOGGED OUT...")
    return redirect("website:home")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.warning(request, "THIS USERNAME ALREADY BEEN USED.")
            return redirect("website:register")
        if form.is_valid():
            password = form.cleaned_data["password"]
            password_confirm = form.cleaned_data["password_confirm"]
            if password == password_confirm:
                user = form.save(commit=False)
                user.set_password(password)
                user.save()
                login(request, user)
                messages.success(request, "YOU ARE REGISTERED ...")
                return redirect("website:home")
            messages.warning(request, "password and confirm password don't match")
            return render(request, "register.html", {"form": form})
    form = RegisterForm()
    return render(request, "register.html", {"form": form})


# @login_required(login_url='website:home', message="YOU SHOULD LOGIN TO BE ABLE TO POST.")
def post_view(request):
    if request.user.is_anonymous:
        messages.warning(request, "YOU SHOULD LOGIN TO BE ABLE TO POST.")
        return redirect("website:home")
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.owner = request.user
            user.save()
            form = PostForm()
            return redirect("website:home")

    form = PostForm()
    return render(request, "post.html", {"form": form})


def record_view(request, pk):
    if request.user.is_anonymous:
        messages.warning(request, "YOU SHOULD LOGIN TO BE ABLE TO POST.")
        return redirect("website:home")

    record = get_object_or_404(Record, id=pk)
    context = {
        "record": record,
    }
    print(record)
    return render(request, "record.html", context)


def delete_view(request, pk):
    if request.user.is_anonymous:
        messages.warning(request, "YOU SHOULD LOGIN TO BE ABLE TO DELETE.")
        return redirect("website:home")
    record = Record.objects.get(id=pk)
    record.delete()
    return redirect("website:home")


def update_view(request, pk):
    if request.user.is_anonymous:
        messages.warning(request, "YOU SHOULD LOGIN TO BE ABLE TO UPDATE.")
        return redirect("website:home")

    record = Record.objects.get(id=pk)
    form = PostForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "FORM BEEN UPDATED SUCCESSFULLY")
        return redirect("website:home")
    return render(request, "post.html", {"form": form})
