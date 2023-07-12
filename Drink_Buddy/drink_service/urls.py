from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name= 'search'),
    path("recipe_detail/<int:id>/", views.recipe_detail, name='drink_service-detail'),
    

    
]