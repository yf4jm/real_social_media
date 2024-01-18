from django.shortcuts import render,get_object_or_404,redirect
from posts.models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/posts'},
        {'GET': '/api/post'}
    ]
    return Response(routes)
@api_view(['GET'])
def getPosts(request):
    posts= Post.objects.all()
    serializer=PostSerializer(posts,many=True)
    return JsonResponse({'posts':serializer.data})
@api_view(['GET'])
def getPost(request,pk):
    try:
        post=Post.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer =PostSerializer(post)
    return Response(serializer.data)
