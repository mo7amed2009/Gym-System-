from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView

urlpatterns=[
    path('sign_up/',views.CreateUserView.as_view(), name='sign_up'),
    path('update_profile/',views.UserProfileUpdateView.as_view(),name='update_profile'),
    path('update_profile_info/',views.UserInfoUpdateView.as_view(),name='update_profile_info'),
    path('my_profile/', views.UserInfoView.as_view() ,name='my_profile'),
    path('users/',views.UsersExersices.as_view(), name='users'),
    path('user_meals/<str:username>/', views.UsersMeals.as_view(), name='user_meals'),
    path('user_meal_items/<str:username>/', views.UserMealItems.as_view(), name='user_meal_items'),
    path('access_token/',TokenObtainPairView.as_view(),name='access_token'),
    path('refresh_token/', TokenRefreshView.as_view(),name='refresh_token')
    
    
    
]