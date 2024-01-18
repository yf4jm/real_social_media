
from django.urls import path
from .views import getPosts,getPost,getRoutes,getComments,getComment,getBadges,getBadge,getCommunities,getCommunity
from .views import getProfiles,getProfile,getHashtags,getHashtag
urlpatterns =[
    path('posts/',getPosts),
    path('post/<str:pk>',getPost),
    path('hashtags/',getHashtags),
    path('hashtag/<str:pk>',getHashtag),
    path('communities/',getCommunities),
    path('community/<str:pk>',getCommunity),
    path('badges/',getBadges),
    path('badge/<str:pk>',getBadge),
    path('profiles/',getProfiles),
    path('profile/<str:pk>',getProfile),
    path('comments/',getComments),
    path('comment/<str:pk>',getComment),



    path('', getRoutes),


]