from django.contrib import admin
from .models import Poll, PollOption, Vote

class PollOptionInline(admin.TabularInline):
    model = PollOption

class PollAdmin(admin.ModelAdmin):
    inlines = [PollOptionInline]
    list_display = ('question', 'created_by', 'created_at', 'start_date', 'end_date')

admin.site.register(Poll, PollAdmin)
admin.site.register(Vote)
