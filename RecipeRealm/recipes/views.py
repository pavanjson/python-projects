from django.shortcuts import get_object_or_404, redirect
from .models import Recipe, RecipeRating
# recipes/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm  # if you're using a form

def home(request):
    recipes = Recipe.objects.all()  # ✅ Get all recipes
    return render(request, 'home.html', {'recipes': recipes})

from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(title__icontains=query)
    else:
        recipes = Recipe.objects.all()

    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def rate_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        rating_value = int(request.POST.get('rating'))
        RecipeRating.objects.update_or_create(
            user=request.user,
            recipe=recipe,
            defaults={'rating': rating_value}
        )
    return redirect('recipe_detail', recipe_id=recipe.id)

@login_required
def rate_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        rating_value = int(request.POST.get('rating'))
        # Update or create the rating
        RecipeRating.objects.update_or_create(
            user=request.user,
            recipe=recipe,
            defaults={'rating': rating_value}
        )
    return redirect('recipe_detail', recipe_id=recipe.id)


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

def all_recipes(request):
    query = request.GET.get('query')
    if query:
        recipes = Recipe.objects.filter(title__icontains=query)
    else:
        recipes = Recipe.objects.all()

    return render(request, 'yourtemplate.html', {'recipes': recipes})