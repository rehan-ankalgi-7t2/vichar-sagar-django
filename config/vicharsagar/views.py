from django.shortcuts import render, redirect
import re
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Article, Topic

# Create your views here.
def home_view(request):
    all_articles = Article.objects.all()
    topics = Topic.objects.all()[:10]
    all_users = User.objects.all()[:10]

    context = {
        "articles": all_articles,
        "topics": topics,
        "users": all_users
    }
    return render(request, "vicharsagar/home.html", context)

def profile_view(request):
    return render(request, "vicharsagar/profile.html")

def list_view(request):
    return render(request, "vicharsagar/lists.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        existing_user = User.objects.filter(username = username)
        if not  existing_user.exists():
            context = {
                "error_message": "User does not exist, please register"
                }
            return render(request, "vicharsagar/login.html", context)
        
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect("home")
            
    return render(request, "vicharsagar/login.html")

def register(request):
    # TODO: explore django messages
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email_address = request.POST.get("email_address")

        # validate email using regex
        email_regex = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9]+$"
        if not re.match(email_regex, email_address):
            return render(request, "vicharsagar/register.html", {"error_message": "Invalid email address."})

        try:
            # check if the user already exists
            existing_user = User.objects.filter(username = username)
            if existing_user.exists():
                context = {
                    "error_message": "User already exists, please log in"
                }
                return render(request, "vicharsagar/register.html", context)

            # Attempting to create  a new user
            new_user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email_address,
                password = password
            )
            new_user.save()

            context = {
                "success_message": "Registration successfull! Please log in."
            }

            return render(request, "vicharsagar/login.html", context)
        
        # handles db integrity errors like, already existing record
        except IntegrityError as e:
            if "username" in str(e):
                context = {
                    "error_message": "Username already exists."
                }
            else:
                context = {
                    "error_message": "Email already in use."
                }
            return render(request, "vicharsagar/register.html", context)
        # catch any other unexpected error / exceptions
        except Exception as e:
            context = {
                "error_message": "An error occurred during registration. Please try again."
                }
            return render(request, "vicharsagar/register.html", context)


    return render(request, "vicharsagar/register.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def about_view(request):
    return render(request, "vicharsagar/about.html")

def contact_view(request):
    return render(request, "vicharsagar/about.html")

def notifications_view(request):
    return render(request, "vicharsagar/about.html",)

def profile_view(request):
    return render(request, "vicharsagar/profile.html")