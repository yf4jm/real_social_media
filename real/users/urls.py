


from django.contrib import admin
from django.urls import path,include
from .views import (signinPage,logoutUser,signupPage)

urlpatterns = [

path("login",signinPage,name="signin"),
path("logout",logoutUser,name="logout"),
path("signup",signupPage,name="signup")

]