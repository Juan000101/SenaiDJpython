from django.urls import path
from .views import home, sobre, receita

urlpatterns = [
    path("", home),
    path("sebre/", sobre),
    path("receitas/", receita),
]
