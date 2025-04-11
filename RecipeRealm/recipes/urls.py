from django.urls import path
from .views import (
    home,
    recipe_list,
    recipe_detail,
    add_recipe,
    rate_recipe,
)

urlpatterns = [
    path('', recipe_list, name='home'),  # 👈 This handles search + homepage
    path('recipes/', recipe_list, name='recipe_list'),  # optional
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/rate/', rate_recipe, name='rate_recipe'),
    path('add/', add_recipe, name='add_recipe'),
]
