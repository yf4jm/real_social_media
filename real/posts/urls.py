from django.urls import path,include
from .views import (create_post,search_by_hashtags,home,
                    c_home,search_by_c_hashtags,power_rankings,
                    post_details,updateproject
)
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("c/<str:community_name>/create_post",create_post,name="create_post"),
    path("c/<str:community_name>/hashtag/<str:hashtag_name>",search_by_c_hashtags,name="search_by_c_hashtags"),
    path("global/hashtag/<str:hashtag_name>",search_by_hashtags,name="search_by_hashtags"),
    path("",home,name="home"),
    path("c/<str:community_name>",c_home,name="c_home"),
    path("leaderboards/communities/<int:page>",power_rankings,name="power_rankings"),
    path("c/<str:community_name>/post/<str:pk>",post_details,name="post_details"),
    path("c/<str:community_name>/update_post/<str:pk>",updateproject,name="updateproject"),
    
    

    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)