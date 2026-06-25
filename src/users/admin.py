from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    
    list_display = ('email', 'username' , 'role')
    
    list_display_links = ('email' , 'username')
    
    list_editable = ('role',)
     
    list_filter =  ('role',)
    
    search_fields = ('username' , 'email')
    
@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    
    list_display = ('age' ,'last_name', 'user' , 'hight' , 'weight' , 'gender' , 'tdee' ,'bmr', 'bmi' , 'activety')
    
    list_editable = ('hight', 'weight' , 'gender'  , 'activety')
    
    list_display_links = ('age' , 'user' , 'last_name')
    
    list_filter = ('age' , 'gender')
    
    search_fields = ('last_name', )
    
   
@admin.register(UserInfo)
class UserInfo(admin.ModelAdmin):
    
    list_display = ('profile' , 'goal', 'target_goal' , 'target_protein_g', 'target_carbs_g', 'target_creatine_g', )
    
    list_display_links = ('profile', )
    
    list_editable = ('goal', )
    
    