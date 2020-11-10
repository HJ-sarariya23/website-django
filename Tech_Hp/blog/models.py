from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    catename = models.CharField(max_length=255)

    def __str__(self):
        return self.catename




class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=15)
    category = models.CharField(max_length=15, default="unknow") 
    slug = models.CharField(max_length=150)
    views = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(blank=True)
    image = models.ImageField( upload_to="",default = "")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + " | " + self.slug

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE , null = True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by "+ self.user.username
    
