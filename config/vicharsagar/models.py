from django.db import models
from django.contrib.auth.models import User  # Assuming user authentication

class Article(models.Model):
    articleTitle = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publishedDate = models.DateField(auto_now_add=True)  # Set on creation
    articleImage = models.ImageField(upload_to='articles/')
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True)
    comments = models.ManyToManyField('Comment', related_name='articles', blank=True)

    def __str__(self):
        return self.articleTitle

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='related_article', on_delete=models.CASCADE)
    commentDescription = models.TextField()
    likes = models.PositiveIntegerField(default=0)  # Use PositiveIntegerField for likes
    replies = models.ManyToManyField('self', blank=True)  # For nested comment replies
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Track comment author

    def __str__(self):
        return f"Comment by {self.user.username} on Article: {self.articles.first().articleTitle}"  # Truncated for brevity

class List(models.Model):
    articles = models.ManyToManyField(Article, related_name='articles_included')  # Many-to-Many relation with articles
    listDescription = models.CharField(max_length=255)
    private = models.BooleanField(default=False)  # Allow creating private lists

    def __str__(self):
        return f"{self.listDescription} List (Private: {self.private})"
    
class Topic(models.Model):
    topicName = models.CharField(max_length=200)

    def __str__(self):
        return self.topicName