from django import forms
from .models import Recipe, RecipeRating


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'image', 'category']

class RatingForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ['rating']