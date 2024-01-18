from rest_framework import serializers
from posts.models import Post,Hashtag,Comment,Community,Badge
from django.contrib.auth.models import User
from users.models import Profile
class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'
        
class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    badge =BadgeSerializer(many=False)
    class Meta:
        model = Profile
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    hashtags=HashtagSerializer(many=True)
    owner=ProfileSerializer(many=False)
    community=CommunitySerializer(many=False)
    likes=ProfileSerializer(read_only=True,many=True)
    class Meta:
        model = Post
        fields = '__all__'
