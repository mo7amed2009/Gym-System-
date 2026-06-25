from rest_framework import serializers
from .models import FoodItem, Meal ,MealItem
from users.models import User

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'name' , 'calories_per_100g' , 'protein_per_100g', 'carbs_per_100g', 'fats_per_100g']
        
class MealSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True , many = False)
    
    class Meta:
        model = Meal
        fields = ['id', 'meal_type', 'user', 'date', 'calories_meal', 'protein_meal', 'carb_meal', 'fats_meal']
        
        
class MealSerializerCreate(serializers.ModelSerializer):
    
    class Meta:
        model = Meal
        fields = ['id', 'meal_type', 'user', 'date', 'calories_meal', 'protein_meal', 'carb_meal', 'fats_meal']
        
class MealItemSerializer(serializers.ModelSerializer):
    meal = serializers.StringRelatedField(read_only=True)
    foods = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = MealItem
        fields = ['id' , 'meal', 'foods', 'weight_in_g', 'calories_food_item', 'protein_food_item', 'carbs_food_item', 'fats_food_item']


class MealItemSerializerCreate(serializers.ModelSerializer):
   
    class Meta:
        model = MealItem
        fields = ['id' , 'meal', 'foods', 'weight_in_g', 'calories_food_item', 'protein_food_item', 'carbs_food_item', 'fats_food_item']