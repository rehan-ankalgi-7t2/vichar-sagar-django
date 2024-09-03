from django.db import models
from django.contrib.auth.models import User  # Assuming user authentication

class Article(models.Model):
    articleTitle = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publishedDate = models.DateField(auto_now_add=True)  # Set on creation
    articleImage = models.ImageField(upload_to='articles/', blank=True, null=True)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True)
    comments = models.ManyToManyField('Comment', related_name='articles', blank=True)
    topics = models.ManyToManyField('Topic', related_name='related_topics', blank=True)

    def __str__(self):
        return self.articleTitle
    
    @property
    def likes_count(self):
        return self.likes.count()
    
    @property
    def comments_count(self):
        return self.comments.count()

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
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Profile picture
    bio = models.TextField(max_length=300, null=True, blank=True)
    push_notification = models.BooleanField(default=True)  # Enabled by default
    email_notification = models.BooleanField(default=True)  # Enabled by default
    theme = models.CharField(max_length=50, blank=True, null=True)  # User interface theme preference
    twitter_handle = models.CharField(max_length=50, blank=True, null=True)  # Twitter username
    facebook_handle = models.CharField(max_length=50, blank=True, null=True)  # Facebook username

    # Relationships (Many-to-Many)
    followers = models.ManyToManyField(User, blank=True, related_name="followers")  # Users following this user
    following = models.ManyToManyField(User, blank=True, related_name="following")  # Users this user follows
    articles = models.ManyToManyField('Article', blank=True, related_name="user_articles")  # User's stories (could be a separate model)
    lists = models.ManyToManyField('List', blank=True, related_name="user_lists")  # User's lists (could be separate models)
    topics = models.ManyToManyField('Topic', blank=True, related_name="user_topics")  # User's followed topics (could be a separate model)

    def __str__(self):
        return str(self.user)
    
    @property
    def profile_field_counts(self):
        total_counts = {
            "followers_count": self.followers.count(),
            "following_count": self.following.count(),
            "articles_count": self.articles.count(),
            "lists_count": self.lists.count(),
            "topics_count": self.topics.count()
        }
        return total_counts