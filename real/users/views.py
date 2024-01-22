
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationForm


# Create your views here.
def signinPage(request):

    if request.user.is_authenticated:
        return redirect('home')


    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        try:
            user =User.objects.get(username=username)
        except:
            messages.error(request, "username or password invalid!")
        user =authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "login successsful!")
            return redirect('home')
    context={}
    return render(request ,"login/login.html",context)
def signupPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occurred during registration')

    context = {"form": form}
    return render(request, "login/signup.html", context)
def logoutUser(request):
    logout(request)
    return redirect('signin')