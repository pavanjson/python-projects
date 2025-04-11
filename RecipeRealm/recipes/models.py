from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Added timestamp field

    def __str__(self):
        return self.title

    def average_rating(self):
        """Calculate the average rating for the recipe."""
        ratings = self.ratings.all()
        if ratings.exists():
            return sum(r.rating for r in ratings) / ratings.count()
        return 0  # Default value if no ratings

    class Meta:
        ordering = ['-created_at']  # ✅ Display newest recipes first


class RecipeRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(default=1)  # Rating scale: 1-5

    class Meta:
        unique_together = ('user', 'recipe')  # Prevent duplicate ratings per user
        db_table = "recipes_rating"  # ✅ Ensuring correct table name
        verbose_name_plural = "Recipe Ratings"  # ✅ Cleaner name in Django Admin

    def __str__(self):
        return f"{self.user.username} rated {self.recipe.title} as {self.rating}/5"
