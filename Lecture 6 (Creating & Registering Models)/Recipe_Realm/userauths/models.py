from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="Users/Profile_images", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Profiles"
    def __str__(self):
        return self.user.username
    def profile_pic(self):
        return mark_safe('<img src="%s" width="50" height="50" />'% (self.profile_image.url))
    def full_name(self):
        return self.user.first_name + " " + self.user.last_name

class Follow(models.Model):
    follower = models.ForeignKey(Profile, related_name = "follower", on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, related_name = "following", on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Followers"
    def __str__(self):
        return self.follower.user.first_name
    def follower_full_name(self):
        return self.follower.user.first_name + " " + self.follower.user.last_name
    def following_full_name(self):
        return self.following.user.first_name + " " + self.following.user.last_name
    