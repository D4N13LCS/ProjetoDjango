from django.urls import path
from recipes.views import MyView, home

urlpatterns = [
    path('sobre/', MyView),
    path('', home),
]