
from django.urls import path
from .views import getPosts,getPost,getRoutes
urlpatterns =[
    path('posts/',getPosts),
    path('post/<str:pk>',getPost),
    path('', getRoutes),


]