from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Restaurant, Recipe, Ingredient
from .serializers import RestaurantSerializer, RecipeSerializer, IngredientSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        recipe_name = self.request.query_params.get('recipe_name', None)
        if recipe_name:
            queryset = queryset.filter(recipes__name=recipe_name)
        return queryset

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        restaurant_id = self.request.query_params.get('restaurant_id', None)
        ingredient_name = self.request.query_params.get('ingredient_name', None)
        if restaurant_id:
            queryset = queryset.filter(restaurant_id=restaurant_id)
        if ingredient_name:
            queryset = queryset.filter(ingredients__name=ingredient_name)
        return queryset

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        recipe_id = self.request.query_params.get('recipe_id', None)
        restaurant_id = self.request.query_params.get('restaurant_id', None)
        if recipe_id:
            queryset = queryset.filter(recipe_id=recipe_id)
        if restaurant_id:
            queryset = queryset.filter(recipe__restaurant_id=restaurant_id)
        return queryset

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
