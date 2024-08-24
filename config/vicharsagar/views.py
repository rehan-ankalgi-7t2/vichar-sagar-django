from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "vicharsagar/home.html")

def profile_view(request):
    return render(request, "vicharsagar/profile.html")

def list_view(request):
    return render(request, "vicharsagar/lists.html")