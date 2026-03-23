from django.contrib import admin
from .models import Task, AppInfo, Profile, OnlineUser

admin.site.register(Task)
admin.site.register(AppInfo)
admin.site.register(Profile)

@admin.register(OnlineUser)
class OnlineUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'connected_at', 'channel_name']
    readonly_fields = ['connected_at']