from django.urls import path
from begin import views
urlpatterns = [
    path('', views.home, name="home")
]
