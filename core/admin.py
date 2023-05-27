from django.contrib import admin
from .models import profiles,LikePost,FollowersCount
from .models import Post
# Register your models here.

admin.site.register(profiles)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)

