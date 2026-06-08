from django.urls import path
from .views import CreateUserView , UserProfileView , UserInfoView


urlpatterns=[
    path('sign_up/',CreateUserView.as_view()),
    path('update_profile/<str:username>/',UserProfileView.as_view()),
    path('update_profile_info/<str:username>/',UserInfoView.as_view()),
    
    
]