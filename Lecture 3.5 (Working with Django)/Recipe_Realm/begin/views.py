from django.shortcuts import render
from begin.models import Recipe
# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes,
    }
    return render(request, "home.html", context)
