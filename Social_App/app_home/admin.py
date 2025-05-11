from django.contrib import admin
from . models import *

admin.site.register(PostImage)

class PostImageAdmin(admin.StackedInline):
    model=PostImage

class PostsAdmin(admin.ModelAdmin):
    inlines=[PostImageAdmin]    

admin.site.register(Posts, PostsAdmin)
admin.site.register(Story)
admin.site.register(FriendRequests)
admin.site.register(Friends)
admin.site.register(Like)
admin.site.register(Comment)
# Register your models here.
