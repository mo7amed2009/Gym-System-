from django.contrib import admin
from .models import Meal , MealItem , FoodItem
# Register your models here.

@admin.register(FoodItem)
class FoodItem(admin.ModelAdmin):
    
    list_display = ('name', 'calories_per_100g', 'protein_per_100g','carbs_per_100g', 'fats_per_100g',)
    
    list_display_links = ('name',)
    
    search_fields = ('name' ,)
    
@admin.register(Meal)
class Meal(admin.ModelAdmin):
    
    list_display = ('user', 'meal_type',  'date', 'calories_meal', 'protein_meal', 'carb_meal', 'fats_meal')
    
    list_display_links = ('user',)
    
    list_editable = ('meal_type', )
    
    list_filter = ('user', 'meal_type')
    
@admin.register(MealItem)
class MealItem(admin.ModelAdmin):
    
    list_display = ('meal', 'foods', 'weight_in_g' , 'calories_food_item' , 'protein_food_item' ,'carbs_food_item', 'fats_food_item')
    
    list_filter = ('meal' , 'foods')