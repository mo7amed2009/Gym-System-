from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Split)
class Split(admin.ModelAdmin):
    
    list_display = ('split_type' ,)
    
    list_display_links = ('split_type' , )
    
    search_fields = ('description',)
    

    
@admin.register(Equipment)    
class Equipment(admin.ModelAdmin):
        
    list_display = ('name' , )
    
    list_display_links = ('name', )
    

@admin.register(SecondryMuscle)    
class SecondryMuscle(admin.ModelAdmin):
        
    list_display = ('name' , )
    
    list_display_links = ('name', )
    
    
@admin.register(Exersice)
class Exersice(admin.ModelAdmin):
    
    list_display = ('name' , 'primary_muscle', 'difcullty')
    
    list_display_links = ('name',)
    
    list_editable = ('difcullty',)
    
    list_filter = ('primary_muscle', 'difcullty',)
    
    search_fields = ('name',)
    
    
@admin.register(ProgramTemlate)
class ProgramTemlate(admin.ModelAdmin):
    
    
    list_display = ('name' , 'level')
    
    list_display_links = ('name',)
    
    list_editable = ('level',)
    
    list_filter = ( 'level',)
    
    search_fields = ('name',)
    
    
@admin.register(ProgramDay)
class ProgramDay(admin.ModelAdmin):
    
    list_display = ('name' , 'program')
    
    list_filter = ( 'program',)
    
    search_fields = ('name',)
    
    
@admin.register(ProgramExersice)
class ProgramExersice(admin.ModelAdmin):
    
    
    list_display =  ('program_day' ,'sets' , 'min_reps' , 'max_reps',)
    
    list_editable = ('sets' , 'min_reps' , 'max_reps')