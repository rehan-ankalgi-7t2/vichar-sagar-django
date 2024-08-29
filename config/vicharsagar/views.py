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
    return render(request, "vicharsagar/register.html")