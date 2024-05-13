from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Recipe(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='recipes', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
