from django.db import models
from django.utils.html import mark_safe
from userauths.models import Profile
from django_quill.fields import QuillField

class Category(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="Categories/Images", null=True, blank=True)
    small_description = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.title
    def category_pic(self):
        return mark_safe('<img src="%s" width="50" height="50" />'% (self.image.url))
    
class Recipies(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recipies")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="Recipies/Images", null=True, blank=True)
    youtube_url = models.URLField(max_length=255, null=True, blank=True)
    content = QuillField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Recipies"
    def __str__(self):
        return self.title
    def recipe_pic(self):
        return mark_safe('<img src="%s" width="50" height="50" />'% (self.image.url))
    
    
class Recipe_Images(models.Model):
    recipe = models.ForeignKey(Recipies, on_delete=models.CASCADE, related_name = "images")
    image = models.ImageField(upload_to="Recipe_other_images")
    class Meta:
        verbose_name_plural = "Recipe Images"
    def __str__(self):
        return self.recipe.title

class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipies, on_delete=models.CASCADE, related_name="likes")
    class Meta:
        verbose_name_plural = "Likes"
    def __str__(self):
        return self.recipe.title

class Review(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipies, on_delete=models.CASCADE)
    review = models.TextField()
    image = models.ImageField(upload_to="Reviews/images", null=True, blank=True)
    rating = models.IntegerField(choices=[(1, "★☆☆☆☆"),(2, "★★☆☆☆"),(3, "★★★☆☆"),(4, "★★★★☆"),(5, "★★★★★"),])
    class Meta:
        verbose_name_plural = "Reviews"
    def __str__(self):
        return self.recipe.title