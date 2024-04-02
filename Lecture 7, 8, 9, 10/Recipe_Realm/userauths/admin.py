from django.contrib import admin
from userauths.models import Profile, Follow

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["profile_pic", "full_name", "bio"]

class FollowAdmin(admin.ModelAdmin):
    list_display = ["follower_full_name", "following_full_name",]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow, FollowAdmin)

