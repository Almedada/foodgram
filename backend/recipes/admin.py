from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Favorite, Ingredient, Recipe, ShoppingCart, Tag


class RecipeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.ingredients.exists():
            raise ValidationError(
                'Рецепт должен содержать хотя бы один ингредиент!'
            )
        if not obj.text:
            raise ValidationError('Описание рецепта обязательно!')
        super().save_model(request, obj, form, change)

    list_display = ('name', 'author', 'cooking_time', 'pub_date')
    search_fields = ('name', 'author__email')
    list_filter = ('tags',)


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user__email', 'recipe__name')


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user__email', 'recipe__name')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Ingredient)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Tag)
