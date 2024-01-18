
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name= models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50,blank=True, null=True)
    short_intro=models.CharField(max_length=160,blank=True, null=True)
    birth_date=models.DateField(blank=True, null=True)
    created_on=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    total_contribution_power = models.FloatField(default=0.0)
    badge =models.ForeignKey('posts.Badge',on_delete=models.DO_NOTHING, null=True, blank=True)
    def __str__(self):
        return str(self.username)
