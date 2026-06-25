from rest_framework import serializers
from .models import User , UserInfo , UserProfile


class UserSerializer(serializers.ModelSerializer):
    """ To Serialize The User Model """    

    class Meta:
        model = User
        fields = ['email' , 'username' , 'password']
        
        
class UserProfileSerializer(serializers.ModelSerializer):
    """ To Serialize UserProfile Model """
    
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'last_name', 'user', 'bio', 'age', 'gender', 'hight', 'weight', 'activety', 'bmi', 'bmr', 'tdee']
        
class UserProfileSerializerCreate(serializers.ModelSerializer):
    """ To Serialize UserProfile Model """
    
    
    class Meta:
        model = UserProfile
        fields = ['id', 'last_name', 'user', 'bio', 'age', 'gender', 'hight', 'weight', 'activety', 'bmi', 'bmr', 'tdee']
        
        
class UserInfoSerializer(serializers.ModelSerializer):
    """ To Serialize UserProfile Model """
    
    profile = serializers.StringRelatedField(read_only = True)
    
    class Meta:
        model = UserInfo
        fields = ['id', 'profile', 'goal', 'is_active', 'target_goal', 'target_protein_g', 'target_fats_g', 'target_carbs_g', 'target_creatine_g']
 
class UserInfoSerializerCreate(serializers.ModelSerializer):
    """ To Serialize UserProfile Model """
    
    
    class Meta:
        model = UserInfo
        fields = ['id', 'profile', 'goal' , 'target_goal', 'target_protein_g', 'target_fats_g', 'target_carbs_g', 'target_creatine_g']
 