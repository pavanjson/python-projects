from django.contrib import admin
from django.urls import path, include,re_path

from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('chat/', include("app_chat.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', include("app_home.urls")),
    path('auth/', include("app_users.urls")),
    path('account/', include("app_account.urls")),
    path('admin/', admin.site.urls),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

