from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Hashtag,Comment,Community
from users.models import Profile
from .forms import PostForm
from django.db.models import Count
from django.http import HttpResponse
from django.db.models import F
from django.contrib import messages
# Create your views here.
def home(request):
    # test git
    community=Community.objects.order_by('-power')[:5]
    context={'community':community}
    return render(request,"home/main.html",context)

def power_rankings(request,page):
    page = int(page)
    community=Community.objects.order_by('-power')[100*(page-1):100*page]
    rank=100*(page-1)
    context={'community':community,'rank':rank}
    return render(request,"leaderboards/community.html",context)

def c_home(request,community_name):
    community = get_object_or_404(Community, slug=community_name)
    posts=Post.objects.filter(community=community)
    context={'community':community,"posts":posts}
    return render(request,"community/main.html",context)

def create_post(request,community_name):
    community = get_object_or_404(Community, name=community_name)
    form = PostForm()
    
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.community= community
            post.save()
            post.extract_and_save_hashtags()
            Community.objects.filter(id=community.id).update(power=F('power') + 0.3)
            Profile.objects.filter(id=Post.owner).update(total_contribution_power=F('total_contribution_power') + 0.3)
            messages.success(request, "Post added successfully!")
            return redirect('c_home',community_name=community_name)

        else:
            form=PostForm()
    
    context={'form':form,'community':community}
    return render(request,"post/create_post.html",context)

def updateproject(request,community_name,pk):
    post=Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form= PostForm(request.POST,instance=post)
        if form.is_valid:
            form.save()
            return redirect('post_details',pk=post.id,community_name=post.community.slug)
    context={'form':form,'post':post}
    return render(request ,"post/update_post.html",context)

def post_details(request,community_name,pk):
    post=Post.objects.get(id=pk)
    context={'post':post}
    return render(request,"post/post.html",context)




def search_by_hashtags(request,hashtag_name):
    try:
        hashtag=Hashtag.objects.get(name=hashtag_name)
    except:
        return HttpResponse('hashtag doesnt exist')
    posts=Post.objects.filter(hashtags=hashtag).annotate(comment_count=Count('comment'))
        
    context={'posts':posts,"hashtag":hashtag}
    return render(request,"hashtag/hashtag_res.html",context)

def search_by_c_hashtags(request,hashtag_name,community_name):
    try:
        hashtag=Hashtag.objects.get(name=hashtag_name)
    except:
        return HttpResponse('hashtag doesnt exist')
    community = get_object_or_404(Community, name=community_name)
    posts=Post.objects.filter(hashtags=hashtag,community=community).annotate(comment_count=Count('comment'))
    
        
    context={'posts':posts,"hashtag":hashtag,'community':community}
    return render(request,"hashtag/hashtag_c_res.html",context)

