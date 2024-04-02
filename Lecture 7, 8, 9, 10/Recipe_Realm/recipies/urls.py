from django.urls import path
from recipies import views
urlpatterns = [
    path("", views.home, name="home"),
    path("recipe/<id>", views.recipe_details, name="recipe_details"),
    path("profile/<id>", views.profile_details, name="profile_details"),
]
