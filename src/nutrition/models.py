from django.db import models
import datetime
from users.models import User ,UserInfo , UserProfile

class FoodItem(models.Model):
    name = models.CharField(unique=True , max_length=65)
    calories_per_100g = models.PositiveIntegerField()
    protein_per_100g = models.DecimalField(max_digits=3 , decimal_places=1)
    carbs_per_100g = models.DecimalField(max_digits=3 , decimal_places=1)
    fats_per_100g = models.DecimalField(max_digits=3 , decimal_places=1, blank=True ,null=True)
    
    def __str__(self):
        return self.name


class Meal(models.Model):
    class ChoiseMeal(models.TextChoices):
        BREAK_FAST = 'Break fast', 'Break fast'
        LUNCH = 'Lunch' , 'Lunch'
        DINNER = 'Dinner' , 'Dinner'
        SNACK = 'Snack' , 'Snack'
        DRINK = 'Drink' , 'Drink'
    
    meal_type = models.CharField(max_length=50, choices=ChoiseMeal.choices)    
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_meal')
    
    date = models.TimeField(null=True , blank=False)
    
    @property
    def calories_meal(self):
        return sum(food.calories_food_item for food in self.foods.all())
    
    @property
    def protein_meal(self):
        return sum(food.protein_food_item for food in self.foods.all())

    @property
    def carb_meal(self):
        return sum(food.carbs_food_item for food in self.foods.all())
        
    @property
    def fats_meal(self):
        return sum(food.fats_food_item for food in self.foods.all())

    
    def __str__(self):
        return f"{self.meal_type} on {self.date} by {self.user.username}"
    
class MealItem(models.Model):
    
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE,related_name='foods')
    
    foods = models.ForeignKey(FoodItem,on_delete=models.CASCADE, )  
    
    weight_in_g = models.DecimalField(max_digits=20,decimal_places=2)
    
    @property
    def calories_food_item(self):
        
        return round((self.foods.calories_per_100g / 100) * self.weight_in_g , 2)
    
    @property
    def protein_food_item(self):
        
        return round((self.foods.protein_per_100g / 100 ) * self.weight_in_g, 2)     
        
    
    @property
    def carbs_food_item(self):
        
        return round((self.foods.carbs_per_100g / 100 ) * self.weight_in_g, 2)
    
    @property
    def fats_food_item(self):
        
       return round((self.foods.fats_per_100g / 100 ) * self.weight_in_g, 2)

    def __str__(self):
        return f"{self.weight_in_g}g of {self.foods.name}"
