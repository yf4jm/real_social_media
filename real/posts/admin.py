from django.contrib import admin
from django.db.models import Count

# Register your models here.
from .models import Hashtag,Comment,Community,Post,Badge,Contribution
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','status', 'like_count','comment_count')
    def like_count(self, obj):
        return obj.likes.all().count()
    def comment_count(self, obj):
        return obj.comment_count
    comment_count.short_description = 'Comment Count'
    comment_count.admin_order_field = 'comment_count'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(comment_count=Count('comment'))
        return queryset
admin.site.register(Hashtag)
admin.site.register(Comment)
admin.site.register(Community)
admin.site.register(Post,InfoAdmin)
admin.site.register(Badge)
admin.site.register(Contribution)
