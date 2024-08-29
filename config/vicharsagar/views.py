from django.shortcuts import render
from .models import Article, Topic
from django.contrib.auth.models import User

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

def login(request):
    return render(request, "vicharsagar/login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            # Attempting to create  a new user
            new_user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
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