"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("notifications/", views.notifications_view, name="notifications"),
    path("profile/edit", views.edit_profile_view, name="edit-profile"),
    path("article/create", views.create_article_view, name="create-article"),
    path("article/<int:article_id>", views.article_details_view, name="view-article"),
    path("article/delete/<int:article_id>", views.delete_article, name="delete-article"),
    path("article/like/<int:article_id>", views.toggle_like_article, name="toggle-like-article"),
    path("list/create", views.create_list_view, name="create-list"),
    path("list/<int:list_id>", views.list_detail_view, name="list-detail"),
]
