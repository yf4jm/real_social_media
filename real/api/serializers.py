from rest_framework import serializers
from posts.models import Post,Hashtag,Comment,Community,Badge,Contribution
from django.contrib.auth.models import User
from users.models import Profile
class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        hashtags_data = validated_data.pop('hashtags', [])
        post = Post.objects.create(**validated_data)
        hashtag_ids = [hashtag_data for hashtag_data in hashtags_data]
        post.hashtags.set(hashtag_ids)
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.media = validated_data.get('media', instance.media)
        instance.hashtags.set(validated_data.get('hashtags', instance.hashtags.all()))
        instance.community = validated_data.get('community', instance.community)
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'

    def create(self, validated_data):
        return Contribution.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.power = validated_data.get('power', instance.power)
        instance.save()
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.short_intro = validated_data.get('short_intro', instance.short_intro)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.total_contribution_power = validated_data.get('total_contribution_power', instance.total_contribution_power)
        instance.badge = validated_data.get('badge', instance.badge)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'