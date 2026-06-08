from rest_framework import serializers
from .models import User , UserInfo , UserProfile


class UserSerializer(serializers.ModelSerializer):
    """ To Serialize The User Model """    

    class Meta:
        model = User
        fields = ['email' , 'username' , 'password']
        
        
class UserProfileSerializer(serializers.ModelSerializer):
    """ To Serialize UserProfile Model """
    
    class Meta:
        model = UserProfile
        fields = '__all__'
        
        
class UserInfoSerializer(serializers.ModelSerializer):
    """ To Serialize UserProfile Model """
    
    class Meta:
        model = UserInfo
        fields = '__all__'
