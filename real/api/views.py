
from posts.models import Post,Hashtag,Comment,Community,Badge,Contribution
from users.models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import (
    CommunitySerializer, BadgeSerializer, HashtagSerializer,
    PostSerializer, CommentSerializer, ContributionSerializer, ProfileSerializer
)

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET/POST': '/api/posts/'},
        {'PUT/DELETE': '/api/posts/'},
        {'GET/POST': '/api/hashtags/'},
        {'PUT/DELETE': '/api/hashtags/'},
        {'GET/POST': '/api/comments/'},
        {'PUT/DELETE': '/api/comments/'},
        {'GET/POST': '/api/communities/'},
        {'PUT/DELETE': '/api/communities/'},
        {'GET/POST': '/api/badges/'},
        {'PUT/DELETE': '/api/badges/'},
        {'GET/POST': '/api/profiles/'},
        {'PUT/DELETE': '/api/profiles/'},

    ]
    return Response(routes)

class CommunityListCreateView(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class CommunityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class BadgeListCreateView(generics.ListCreateAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

class BadgeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

class HashtagListCreateView(generics.ListCreateAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

class HashtagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ContributionListCreateView(generics.ListCreateAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

class ContributionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
