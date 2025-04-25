from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Favorite, Ingredient, Recipe, ShoppingCart, Tag


class IngredientAdmin(admin.ModelAdmin):
    search_fields = ['name']


class RecipeAdmin(admin.ModelAdmin):
    def get_favorites_count(self, obj):
        return obj.favorite.count()
    get_favorites_count.short_description = 'Число в избранном'

    list_display = (
        'name', 'author', 'cooking_time', 'pub_date', 'get_favorites_count'
    )
    search_fields = ('name', 'author__email')
    list_filter = ('tags',)

    def save_model(self, request, obj, form, change):
        if not obj.ingredients.exists():
            raise ValidationError(
                'Рецепт должен содержать хотя бы один ингредиент!'
            )
        if not obj.text:
            raise ValidationError('Описание рецепта обязательно!')
        super().save_model(request, obj, form, change)


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user__email', 'recipe__name')


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user__email', 'recipe__name')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Tag)
