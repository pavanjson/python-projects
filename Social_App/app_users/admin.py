from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ('email', 'username','is_staff')
#     search_fields = ('email', 'username')
#     ordering = ('email',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('username', 'first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'username', 'password1', 'password2'),
#         }),
#     )

admin.site.register(User)
admin.site.register(Profile)
