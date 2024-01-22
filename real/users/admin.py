from django.contrib import admin
from .models import Profile

# Register your models here

class InfoAdmin(admin.ModelAdmin):
    list_display = ('id','username','total_contribution_power',"created_on")
admin.site.register(Profile,InfoAdmin)
