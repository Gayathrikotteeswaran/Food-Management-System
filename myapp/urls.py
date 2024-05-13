from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, RecipeViewSet, IngredientViewSet


router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)


urlpatterns = [
    path('', include(router.urls)),  # Includes router generated URL
]
