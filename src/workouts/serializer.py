from rest_framework import serializers
from .models import *

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name' ,'description']

class SecondryMuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondryMuscle
        fields = ['id', 'name' ,'description']
        
class ExersiceSerializer(serializers.ModelSerializer):
    secondry_muscle = serializers.StringRelatedField(many=True , read_only=True) # To Show All Secondary Muscles At List
    
    equipment = serializers.StringRelatedField(many=True , read_only=True) # To Show All Equipments At List 
    
    class Meta:
        model = Exersice
        fields = ['id' , 'name' , 'primary_muscle' , 'secondry_muscle' , 'equipment' , 'difcullty' , 'video']

class SpiltSerializer(serializers.ModelSerializer):
    class Meta:
        model = Split
        fields = ['id' , 'split_type' , 'description']
        
        

class ProgramTemlateSerializer(serializers.ModelSerializer):
    
    split = serializers.StringRelatedField(read_only=True)  # To Show Split Name Of It Program
    
    class Meta:
        model = ProgramTemlate
        fields = ['id', 'name' , 'split' , 'level' , 'description']
        
        
        
class ProgramDaySerializer(serializers.ModelSerializer):
    
    program = serializers.StringRelatedField(read_only=True) # To Show Program Tempalte Name Of It Program
    
    
    class Meta:
        model = ProgramDay
        fields = ['id' , 'name' ,'program' , 'order']


class ProgramExrsiceSerializer(serializers.ModelSerializer):
    
    exersice = serializers.StringRelatedField(many=True , read_only=True)  # To Show All Exersices Name 
    
    program_day = serializers.StringRelatedField(read_only=True) # To Show Program Day Name
    
    class Meta:
        model = ProgramExersice
        fields = ['id' ,'slug' , 'program_day' ,'exersice', 'min_reps', 'max_reps' , 'sets' , 'order']