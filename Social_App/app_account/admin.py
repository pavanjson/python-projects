from django.contrib import admin
from . import models as mdl

admin.site.register(mdl.NoticeCategory)
admin.site.register(mdl.Notification)