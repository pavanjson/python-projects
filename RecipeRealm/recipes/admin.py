from django.contrib import admin
from .models import Recipe, RecipeRating


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_at']  # ✅ Fix: Ensure this field exists

admin.site.register(Recipe, RecipeAdmin)

@admin.register(RecipeRating)
class RecipeRatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'rating')
