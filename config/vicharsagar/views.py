from django.shortcuts import render
from .models import Article

# Create your views here.
def home_view(request):
    all_articles = Article.objects.all()
    return render(request, "vicharsagar/home.html", {'articles': all_articles})

def profile_view(request):
    return render(request, "vicharsagar/profile.html")

def list_view(request):
    return render(request, "vicharsagar/lists.html")