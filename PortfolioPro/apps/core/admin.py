from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'facebook', 'instagram', 'whatsapp')
    search_fields = ('user__username', 'title')
    list_filter = ('title',)
    ordering = ('user__username',)

    # To edit fields directly in admin panel
    fields = ('user', 'title', 'description', 'facebook', 'instagram', 'whatsapp', 'image')

admin.site.register(Profile, ProfileAdmin)
