from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import FoodItem, Meal ,MealItem
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import *
from users.views import IsCoach 
# Create your views here.


        
class MealUserView(APIView):
    # authentication_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    
    def get(self, request, *warg , **kwargs):
        try:
        
            meal_user = Meal.objects.filter(user=request.user,meal__user__role="Trainee")
            
        except:
            return Response({'massege':'Error User Not Found'},status=status.HTTP_400_BAD_REQUEST)
        
        data = [
            {
                'name': meal.user.username,
                'meal': meal.meal_type,
                'date meal': meal.date,
                'calories meal': meal.calories_meal,
                'protein meal': meal.protein_meal,
                'carb meal': meal.carb_meal,
                'fats meal': meal.fats_meal,
                
            }
            for meal in meal_user
        ]
        return Response(data,status=status.HTTP_100_CONTINUE)
    
    
    
    
class MealItemUserView(APIView):
    # authentication_classes = [IsAuthenticated  ]
    # authentication_classes = [JWTAuthentication]
    
    def get (self, request , *wargs , **kwargs):
        try:
            
            meal_item = MealItem.objects.filter(meal__user = request.user,meal__user__role="Trainee")
        except:
            return Response({"massege":"The User Of This Diet Not Found"})
            
        data = [
            {
                "meal":item.meal,
                'food':item.foods,
                'weight in gram':item.weight_in_g,
                'calories food item':item.calories_food_item,
                'protein food': item.protein_food_item,
                'carbs food': item.carbs_food_item,
                'fats food': item.fats_food_item
                
            } for item in meal_item 
        ] 
        
        return Response(data,
                        status=status.HTTP_100_CONTINUE)
        
        
    
class CreateDietPlanView(APIView):
    
    def post(self , request , *wars , **kwargs):
        
        serialize = MealItemSerializerCreate(data = request.data)
        
        if serialize.is_valid():
            serialize.save()
        
            return Response({"massege":"Created Successfuly"} 
                            ,status=status.HTTP_201_CREATED)
            
        return Response({"massege":'This Not Valid'},
                status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
class UpdateDietPlanView(APIView):
    
    def put (self , request , meal_type, username ,  *wars , **kwargs):
        try:
        
            user = Meal.objects.get(user__username__exact=username , meal_type=meal_type)
        except:
            return Response({"massege":"User Not Found"},
                            status=status.HTTP_404_NOT_FOUND)
        
        serialize = MealSerializerCreate(user, data=request.data)
        
        if serialize.is_valid():
            serialize.save()
            
            return Response({"massege":'Updates Succssfuly'},status=status.HTTP_200_OK)
        
        return Response({"massege":'This Not Valid'},
                        status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
class DeleteDietPlanView(APIView):
    
    def delete(self , request , meal_type, username ,  *wars , **kwargs):
        try:
        
            user = Meal.objects.get(user__username__exact=username , meal_type=meal_type)
        except:
            return Response({"massege":"User Not Found"},
                            status=status.HTTP_404_NOT_FOUND)
        user.delete()
        
        return Response({'massege':'Deleted Successfuly'})




class CreateFood(generics.ListCreateAPIView):
    
    # permission_classes = [IsCoach | IsAdminUser] 
    
    # authentication_classes = [JWTAuthentication]
    
    queryset = FoodItem.objects.all()
    
    serializer_class = FoodItemSerializer
    
    
    
class UpdateFood(generics.UpdateAPIView):
    
    # permission_classes = [IsCoach | IsAdminUser] 
    
    # authentication_classes = [JWTAuthentication]
    
    queryset = FoodItem.objects.all()
    
    serializer_class = FoodItemSerializer
    
    lookup_field = 'name'
    

class DeleteFood(generics.DestroyAPIView):
    
    # permission_classes = [IsAdminUser] 
    
    # authentication_classes = [JWTAuthentication]
    
    queryset = FoodItem.objects.all()
    
    serializer_class = FoodItemSerializer  

    lookup_field = 'name'






class UpdateMealItemView(generics.UpdateAPIView):
    
    # permission_classes = [IsAdminUser | IsCoach] 
    
    # authentication_classes = [JWTAuthentication]
    
    queryset = MealItem.objects.all()
    
    serializer_class = MealItemSerializerCreate
    
    lookup_field = 'id'
    
    
    
    

class DeletMealItemView(generics.DestroyAPIView):
    
    # permission_classes = [IsAdminUser] 
    
    # authentication_classes = [JWTAuthentication]
    
    queryset = MealItem.objects.all()
    
    serializer_class = MealSerializerCreate
    
    lookup_field = 'id'
    
      
class CreateMealItemView(generics.ListCreateAPIView):
    
    # permission_classes = [IsAdminUser | IsCoach] 
    
    # authentication_classes = [JWTAuthentication]
    
    queryset = MealItem.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MealItemSerializerCreate
        
        return MealItemSerializer        