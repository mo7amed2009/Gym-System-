from django.shortcuts import render
from rest_framework import generics
from .models import User , UserInfo , UserProfile
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , IsAdminUser ,BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from nutrition.models import MealItem ,Meal ,FoodItem
from nutrition.serializer import FoodItemSerializer
from django.contrib.auth.hashers import make_password
# Create your views here.

class IsAdmin(BasePermission):
    
    def has_permission(self , request , view):
        
        return request.user and request.user.role == 'Admin' and  request.user.is_authenticated

class IsCoach(BasePermission):
    
    def has_permission(self , request , view):
        
        return request.user and request.user.role == 'Coach' and  request.user.is_authenticated
    


class CreateUserView(APIView):
    def post(self, request , *wargs , **kwargs):
    
        email = request.data.get('email')
        password = request.data.get("password")
        username = request.data.get("username")
        
        if not email or not password :
            return Response({'Error':"All This Is Required"}) 
        
        elif User.objects.filter(email=email).exists() :
            return Response({'Error':"This email Aready Exist"})
        
        
        elif User.objects.filter(username=username).exists() :
            return Response({'Error':"This username Aready Exist"})
        
        user = User.objects.create(
            email = email,
            password = make_password(password),
            username = username,
        
            
        )
        user.save()
        
        return Response({'massege':"User Created Successfuly"})
        
    
    
    
class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated  ]
    authentication_classes = [JWTAuthentication]

    
    def put(self , request  , *wargs , **kwargs):
        
        try:
        
            query = UserProfile.objects.get(user=request.user)
        
        except:
            return Response({"Massege":"Not Found"} ,status=status.HTTP_404_NOT_FOUND)    
            
        
        serializer = UserProfileSerializerCreate(query,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({"Massege":"The Profile Of You Updated Successfuly"},
                            status=status.HTTP_202_ACCEPTED)
            
        return Response(serializer.errors)    
    
    
    
class UserInfoUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def put(self , request , *wargs , **kwargs):
        
        try:
        
            query = UserInfo.objects.get(profile__user=request.user)
        
        except:
            return Response({"Massege":"Not Found"} ,status=status.HTTP_404_NOT_FOUND)    
            
        serializer = UserInfoSerializerCreate(query,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({"Massege":"The Profile Info Of You Updated Successfuly"},
                            status=status.HTTP_202_ACCEPTED)
            
        return Response(serializer.errors)    
        
        
        
class UserInfoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated ]
    
    def get(self , request , *wargs , **kwargs):
        
        try:
            query1 = UserInfo.objects.get(profile__user=request.user)
        
            query2 = UserProfile.objects.get(user=request.user)
            
        except:
            return Response({'massege':'Error User Not Find'},status=status.HTTP_400_BAD_REQUEST)

        data = {
            'name' : query2.user.username,
            'your Goal':query1.goal,
            'your Body': query2.bmi,
            'your Calories': query2.tdee,
            'protein Day':query1.target_protein_g,
            'Carb Day':query1.target_carbs_g,
            'fats Day':query1.target_fats_g,
            'creatine Day':query1.target_creatine_g
            
                
        }
        
        return Response(data,status=status.HTTP_100_CONTINUE)
    

class UsersExersices(APIView):
  
    authentication_classes = [JWTAuthentication]
    
    permission_classes = [IsAdminUser]
    
    def get(self , request , *wargs , **kwargs):
        try:
            users = UserInfo.objects.filter(profile__user__role='Trainee')
            

        except:
            return Response({"massege":"No Users in This"})
        
        data = [
            {
            "id": user.pk,
            'is_active':user.is_active,
            "name":user.profile.user.username,
            "last_name":user.profile.last_name,
            "email":user.profile.user.email,
            "gender":user.profile.gender,
            'age':user.profile.age,
            'hight':user.profile.hight,
            'weight':user.profile.weight,
            'activety':user.profile.activety,
            'bmi':user.profile.bmi,
            'bmr':user.profile.bmr,
            'tdee':user.profile.tdee,
            'goal':user.goal,
            'target_tdee':user.target_goal,
            'target_protein':user.target_protein_g,
            'target_carb':user.target_carbs_g,
            'target_fats':user.target_fats_g,
            'target_creatine':user.target_creatine_g,
     
        }
           for user in  users  ]
        
        return Response(data, status=status.HTTP_200_OK)
        

class UsersMeals(APIView):
    authentication_classes = [JWTAuthentication]
    
    permission_classes = [IsAdminUser]
    
    
    def get(self , request ,username ,  *wargs , **kwargs):
        try:
            users_diet = Meal.objects.filter(user__role='Trainee',user__username__exact=username)
            
            mealitems = MealItem.objects.filter(meal__user__role="Trainee")
            
        except:
            return Response({"massege":"No Users in This"})
        
        data = [
            {
                "id":user.user.pk,
                "is_active":user.user.is_active,
                'name':user.user.username,
                'meal':user.meal_type,
                'date': user.date,
                'calories meal': user.calories_meal,
                'protein meal': user.protein_meal,
                'carbs meal': user.carb_meal,
                'fats meal': user.fats_meal,
                
                
            } for user in users_diet
        ]
        
        return Response(data, status=status.HTTP_200_OK)

class UserMealItems(APIView):
    authentication_classes = [JWTAuthentication]
    
    permission_classes = [IsAdminUser]
    
    
    def get(self , request ,username ,  *wargs , **kwargs):
        try:
            mealitems = MealItem.objects.filter(meal__user__role="Trainee",meal__user__username=username,)
        
        except:
            return Response({"massege":"Error User Not Found"})

        data = [
            {
              'user':item.meal.user.username,
              'id':item.meal.user.pk ,
              'is_active': item.meal.user.is_active,
              'meal':item.meal,
              'food':item.foods,
              'weight in g':item.weight_in_g,
              'calories food ':item.calories_food_item,
              'protein_food_item':item.protein_food_item,
              'carbs food_item':item.carbs_food_item,
              'fats_food_item':item.fats_food_item,
              
                
                
                
            } for item in mealitems
        ]
        return Response(data, status=status.HTTP_200_OK)
        