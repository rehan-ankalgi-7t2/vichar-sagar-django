from django import forms
from .models import Profile, Article, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pfp', 'bio', 'push_notification', 'email_notification', 'twitter_handle', 'facebook_handle']
        widgets={
            'pfp': forms.ClearableFileInput(attrs={'class': 'block'}),
            'bio': forms.Textarea(attrs={'class': 'w-[100%] block rounded-md', 'rows': 5, 'cols': 100, 'placeholder': 'Write your bio here...'}),
            'twitter_handle': forms.TextInput(attrs={'class': 'border-2 focus:border-4 focus:border-blue-500 rounded-md block w-full'}),
            'facebook_handle': forms.TextInput(attrs={'class': 'border-2 focus:border-4 focus:border-blue-500 rounded-md block w-full'})
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['articleTitle', 'content', 'topics', 'articleImage']
        widgets={
            'articleTitle': forms.TextInput(attrs={'class': 'border-2 focus:border-4 focus:border-blue-500 rounded-md block w-[100%]'}),
            'content': forms.Textarea(attrs={'class': 'w-[100%] block rounded-md', 'rows': 5, 'cols': 100, 'placeholder': 'Write your bio here...'}),
            'topics': forms.CheckboxSelectMultiple(attrs={'class': 'border-2 focus:border-4 focus:border-blue-500 rounded-md'}),
            'articleImage': forms.ClearableFileInput(attrs={'class': 'block'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commentDescription']
        widgets={
            'commentDescription': forms.TextInput(attrs={'class': 'border-2 focus:border-4 focus:border-blue-500 rounded-md block w-full'})
        }
