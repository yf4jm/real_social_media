from django.db import models
import uuid
from django.contrib.auth.models import User
from users.models import Profile
from django.utils.text import slugify
import re
# Create your models here.
class Community(models.Model):
    name=models.CharField(max_length=20)
    slug=models.SlugField(default="",null=False)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Community, self).save(*args, **kwargs)
    power=models.FloatField(default=0)
    image=models.ImageField(null=True, blank=True,default="default.jpg",upload_to="images")
    def __str__(self):
        return self.slug


class Badge(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.ImageField(null=True, blank=True)
    c_requirement=models.FloatField(default=0)
    def __str__(self):
        return self.name

class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name



class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True, blank=True,related_name='owned_posts')
    title = models.CharField(max_length=50,null=True, blank=True)
    description =models.TextField(max_length=500)
    media = models.ImageField(null=True, blank=True,upload_to='images/')
    hashtags =models.ManyToManyField(Hashtag,blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    community=models.ForeignKey(Community,on_delete=models.CASCADE,null=True,blank=True)
    likes = models.ManyToManyField(Profile, blank=True,related_name='liked_posts')
    

    def extract_and_save_hashtags(self):
        hashtags = re.findall(r'#(\w+)', self.description)
        for hashtag_name in hashtags:
            hashtag, created = Hashtag.objects.get_or_create(name=hashtag_name)
            self.hashtags.add(hashtag)
class Comment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User, blank=True)
    comment=models.CharField(max_length=500)

class Contribution(models.Model):
    contributer=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)
    power=models.FloatField(default=0.0)
    Community=models.ForeignKey(Community,on_delete=models.DO_NOTHING,null=True,blank=True)

