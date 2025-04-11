from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),       # 👈 Main app
    path('accounts/', include('accounts.urls')),  # Login/register
]
handler404 = 'eventease.views.custom_404'