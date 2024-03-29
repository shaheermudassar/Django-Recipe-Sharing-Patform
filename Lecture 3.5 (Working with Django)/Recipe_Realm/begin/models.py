from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="recipe/images/")
    def __str__(self):
        return self.title
    