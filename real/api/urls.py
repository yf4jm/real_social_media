
from django.urls import path
# from .views import getPosts,getPost,getRoutes,getComments,getComment,getBadges,getBadge,getCommunities,getCommunity
# from .views import getProfiles,getProfile,getHashtags,getHashtag
from .views import (
                getRoutes,CommunityListCreateView, CommunityDetailView,
                BadgeListCreateView, BadgeDetailView,
                HashtagListCreateView, HashtagDetailView,
                PostListCreateView, PostDetailView,
                CommentListCreateView, CommentDetailView,
                ContributionListCreateView, ContributionDetailView,
                ProfileListCreateView, ProfileDetailView,UserListCreateView,UserDetailView
                    
                    )
urlpatterns =[
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('communities/', CommunityListCreateView.as_view(), name='community-list-create'),
    path('communities/<uuid:pk>/', CommunityDetailView.as_view(), name='community-detail'),

    path('badges/', BadgeListCreateView.as_view(), name='badge-list-create'),
    path('badges/<int:pk>/', BadgeDetailView.as_view(), name='badge-detail'),

    path('hashtags/', HashtagListCreateView.as_view(), name='hashtag-list-create'),
    path('hashtags/<int:pk>/', HashtagDetailView.as_view(), name='hashtag-detail'),

    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<uuid:pk>/', CommentDetailView.as_view(), name='comment-detail'),

    path('contributions/', ContributionListCreateView.as_view(), name='contribution-list-create'),
    path('contributions/<int:pk>/', ContributionDetailView.as_view(), name='contribution-detail'),

    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<uuid:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('', getRoutes),


]