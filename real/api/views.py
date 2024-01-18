from django.shortcuts import render,get_object_or_404,redirect
from posts.models import Post,Hashtag,Comment,Community,Badge
from users.models import Profile
from .serializers import PostSerializer,HashtagSerializer,CommunitySerializer,BadgeSerializer,ProfileSerializer,CommentSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

class PostRS:
    def __init__(self,id,title,description,media,community,owner,hashtags):
        self.id=id
        self.title=title
        self.description=description
        self.media=media
        self.community=community
        self.owner=owner
        self.hashtags=hashtags
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/posts'},
        {'GET': '/api/post'},
        {'GET': '/api/hashtags'},
        {'GET': '/api/hashtag'},
        {'GET': '/api/comments'},
        {'GET': '/api/comment'},
        {'GET': '/api/communities'},
        {'GET': '/api/community'},
        {'GET': '/api/badges'},
        {'GET': '/api/badge'},
        {'GET': '/api/profiles'},
        {'GET': '/api/profile'},

    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def getPosts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse({'posts': serializer.data})
    
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getPost(request,pk):
    try:
        post=Post.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer =PostSerializer(post)
    return Response(serializer.data)

@api_view(['GET'])
def getHashtags(request):
    hashtags= Hashtag.objects.all()
    serializer=HashtagSerializer(hashtags,many=True)
    return JsonResponse({'hashtags':serializer.data})

@api_view(['GET'])
def getHashtag(request,pk):
    try:
        hashtag=Hashtag.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer =HashtagSerializer(hashtag)
    return Response(serializer.data)


@api_view(['GET','POST'])
def getCommunities(request):
    if request.method=='GET':
        communities= Community.objects.all()
        serializer=CommunitySerializer(communities,many=True)
        return JsonResponse({'Communities':serializer.data})
    if  request.method=='POST':
        serializer=CommunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def getCommunity(request,pk):
    try:
        community=Community.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer =CommunitySerializer(community)
    return Response(serializer.data)

@api_view(['GET'])
def getBadges(request):
    Badges= Badge.objects.all()
    serializer=BadgeSerializer(Badges,many=True)
    return JsonResponse({'Badges':serializer.data})

@api_view(['GET'])
def getBadge(request,pk):
    try:
        badge=Badge.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer =BadgeSerializer(badge)
    return Response(serializer.data)
@api_view(['GET'])
def getProfiles(request):
    profiles= Profile.objects.all()
    serializer=ProfileSerializer(profiles,many=True)
    return JsonResponse({'Profiles':serializer.data})


@api_view(['GET'])
def getProfile(request,pk):
    try:
        profile=Profile.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer =ProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['GET'])
def getComments(request):
    comments= Comment.objects.all()
    serializer=CommentSerializer(comments,many=True)
    return JsonResponse({'comments':serializer.data})

@api_view(['GET'])
def getComment(request,pk):
    try:
        comment=Comment.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer =CommentSerializer(comment)
    return Response(serializer.data)

