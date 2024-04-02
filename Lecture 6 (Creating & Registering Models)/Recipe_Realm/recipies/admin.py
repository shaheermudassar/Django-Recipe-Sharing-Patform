from django.contrib import admin
from recipies.models import Category, Recipies, Recipe_Images, Like, Review

class RecipeImagesInlineStack(admin.TabularInline):
    model = Recipe_Images

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_pic", "title"]

class LikeAdmin(admin.ModelAdmin):
    list_display = ["recipe", "profile"]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["recipe", "profile", "rating"]

class RecipiesAdmin(admin.ModelAdmin):
    inlines = [RecipeImagesInlineStack]
    list_display = ["recipe_pic", "title", "profile", "category"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipies, RecipiesAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Review, ReviewAdmin)
