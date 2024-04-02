from django.shortcuts import render
from recipies.models import Recipies, Category, Review, Like
from userauths.models import Profile

def home(request):
    recipies = Recipies.objects.all().order_by('?')[:6]
    categories = Category.objects.all().order_by('?')[:5]
    profiles = Profile.objects.all().order_by('?')[:4]

    context = {
        "recipies": recipies,
        "categories": categories,
        "profiles": profiles,
    }
    return render(request, "home.html", context)

def recipe_details(request, id):
    recipe = Recipies.objects.get(id=id)
    reviews = Review.objects.filter(recipe=recipe)
    related_recipies = Recipies.objects.filter(profile = recipe.profile)[:3]
    context = {
        "recipe": recipe,
        "reviews": reviews,
        "related_recipies": related_recipies,
    }
    return render(request, "recipe-details.html", context)

def profile_details(request, id):
    profile = Profile.objects.get(id = id)
    number_of_likes = Like.objects.filter(recipe__profile = profile).count()
    context = {
        "profile": profile,
        "number_of_likes": number_of_likes,
    }
    return render(request, "profile-details.html", context)