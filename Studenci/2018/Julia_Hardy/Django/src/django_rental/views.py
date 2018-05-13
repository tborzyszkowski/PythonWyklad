from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import logout
from django.conf import settings

def home_page(request):
    context = {
        "title": "Home",
        "content": "Welcome to home page"
    }
    return render(request, "home/home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "contact page",
        "content": "Welcome to contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)# po submit zostaja dane widoczne
    return render(request, "contact/view.html", context)



def grafik(request):
    context = {
        "title": "grafik",
        "content": "Welcome to grafik page"
    }
    return render(request, "grafik/grafik.html", context)

def cennik(request):
    context = {
        "title": "cennik",
        "content": "Welcome to cennik page"
    }
    return render(request, "cennik/cennik.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context ={
        "form": form
    }
    print("User logged in")
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")# przypisujemy do uzytkownika
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Error")

    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context ={
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)


def logout_page(request):
    logout(request)
    return render(request, "home/home_page.html")

