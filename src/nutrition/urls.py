from django.urls import path
from . import views



urlpatterns=[
    path('your_meals/', views.MealUserView.as_view() , name='meal_user'),
    path('your_meals_items/', views.MealItemUserView.as_view() , name='meal_user_items'),
    path('insert_food/', views.CreateFood.as_view(), name='create_food'),
    path('update_food/<str:name>/', views.UpdateFood.as_view(), name='update_food'),
    path('delete_food/<str:name/', views.DeleteFood.as_view(), name='delete_food'),
    path('createlist_meal_items/', views.CreateMealItemView.as_view(), name="createlist_meal_items"),
    path('update_meal_items/<int:id>/', views.UpdateMealItemView.as_view(), name="update_meal_items"),
    path('delete_meal_items/<int:id>/', views.DeletMealItemView.as_view(), name="delete_meal_items"),
    path('create_meal_user/', views.CreateDietPlanView.as_view() , name='create_meal_user'),
    path('update_meal_user/<str:meal_type>/user/<str:username>/', views.UpdateDietPlanView.as_view() , name='update_meal_user'),
    path('delete_meal_user/<str:meal_type>/user/<str:username>/', views.DeleteDietPlanView.as_view() , name='delete_meal_user'),
    
    
]