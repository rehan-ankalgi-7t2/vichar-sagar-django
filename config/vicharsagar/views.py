from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, get_list_or_404
import re
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Article, Topic, Profile, Comment, List
from .forms import ProfileForm, ArticleForm, CommentForm, CreateListForm

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

            # create a new profile and attach new user to it
            new_profile = Profile.objects.create(
                user = new_user
            )

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
    if request.user.is_authenticated:
        # the user is logged in
        existing_profile = get_object_or_404(Profile, user=request.user.id)
        authored_articles = Article.objects.filter(author = request.user)
        user_lists = List.objects.filter(user = request.user)

        if existing_profile:
            context = {
                "user_data": request.user,
                "profile_data": existing_profile,
                "user_articles": authored_articles,
                "user_lists": user_lists
            }
        else:
            context = {
                "message": "your profile is not complete",
                "user_data": request.user
            }
    else:
        # user not logged in
        context = {
            "message": "you are not logged in."
        }
    return render(request, "vicharsagar/profile.html", context)

def edit_profile_view(request):
    try:
        current_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        current_profile = None

    if request.method == 'POST':
        if current_profile:
            form = ProfileForm(request.POST, request.FILES, instance=current_profile)
        else:
            form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Associate the profile with the current logged-in user

            # Handle profile picture - retain the existing one if no new one is uploaded
            if 'pfp' not in request.FILES and current_profile:
                profile.pfp = current_profile.pfp

            profile.save()
            messages.success(request, 'Your profile was successfully updated!')
            print(profile)
            return redirect('profile')
    else:
        if current_profile:
            form = ProfileForm(instance=current_profile)
        else:
            form = ProfileForm()

    return render(request, "vicharsagar/edit_profile.html", {'form': form})

def create_article_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            messages.success(request, 'Your article  was successfully published!')
            return redirect('home')
    else:
        form = ArticleForm()

    return render(request, "vicharsagar/create_article.html", {'form': form})

def article_details_view(request, article_id):
    isUserAuthor = False
    isLiked = False
    curr_article = get_object_or_404(Article, pk=article_id)
    article_author = get_object_or_404(User, pk=curr_article.author.id)
    author_profile = get_object_or_404(Profile, user=article_author.id)
    article_comments = Comment.objects.filter(article = article_id)

    if(request.user in curr_article.likes.all()):
        isLiked = True
    
    if request.user == article_author:
        isUserAuthor = True
    

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.article = curr_article
            new_comment.save()
            messages.success(request, 'comment shared successfully')

            # Redirect to the same article page to avoid form resubmission
            return redirect('view-article', article_id=article_id)
    else:
        form = CommentForm()

    context = {
        "article_data": curr_article,
        "author_data": article_author,
        "author_profile": author_profile,
        "comments": article_comments or [],
        "isUserAuthor": isUserAuthor,
        "isLiked": isLiked,
        "comments_count": len(article_comments),
        "form": form
    }

    return render(request, "vicharsagar/view_article.html", context)

def delete_article(request, article_id):
    curr_article = Article.objects.get(id=article_id)
    curr_article.delete()
    return redirect('home')

def create_list_view(request):
    if request.method == 'POST':
        form = CreateListForm(request.POST)

        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user
            new_list.save()
            messages.success(request, 'Your list  was successfully created!')
            return redirect('home')
    else:
        form = CreateListForm()

    return render(request, "vicharsagar/create_list.html", {'form': form})

def list_detail_view(request, list_id):
    isOwner = False
    current_list = get_object_or_404(List, pk=list_id)
    list_owner = get_object_or_404(User, pk=current_list.user.id)
    list_owner_profile = get_object_or_404(Profile, user=current_list.user.id)
    list_articles = current_list.articles.all()
    # list_articles = get_list_or_404(Article, id in current_list.art)
    
    if request.user == list_owner:
        isOwner = True

    context = {
        "list_data": current_list,
        "list_articles": list_articles or [],
        "list_owner": list_owner,
        "list_owner_profile": list_owner_profile,
        "isOwner": isOwner
    }

    return render(request, "vicharsagar/list_detail.html", context)

@login_required
def toggle_like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user

    if user in article.likes.all():
        article.likes.remove(user)  # Unlike the article
    else:
        article.likes.add(user)  # Like the article

    return redirect('view-article', article_id=article.id)

@login_required
def toggle_article_in_list(request, list_id, article_id):
    current_list = get_object_or_404(List, pk=list_id)
    current_article = get_object_or_404(Article, pk=article_id)

    if current_article in current_list.articles.all():
        current_list.articles.remove(current_article)
    else:
        current_list.articles.add(current_article)

    return redirect('view-article', article_id=article_id)