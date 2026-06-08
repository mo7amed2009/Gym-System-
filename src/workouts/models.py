from django.db import models
from django.core.validators import MaxLengthValidator , MinLengthValidator
import uuid


class Level (models.TextChoices):

    
    BEGAINER = "beginner" , "Breinner"
    
    INTERMEDIATE = "intermediate" , "Intermediate"
    
    ADVANCED = "advanced" , "Advanced"
    
    PROFISIONAL = 'profisional' , 'Profisional'
    
class Equipment(models.Model):

    name =models.CharField(max_length=50)
    
    description = models.TextField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class PrimaryMuscle(models.TextChoices):
    CHEST = "CHEST", "Chest"
    BACK = "BACK", "Back"
    SHOULDERS = "SHOULDERS", "Shoulders"
    BICEPS = "BICEPS", "Biceps"
    TRICEPS = "TRICEPS", "Triceps"
    LEGS = "LEGS", "Legs"
    ABS = "ABS", "Abs"
    CALVES = "CALVES", "Calves"
    


class SecondryMuscle(models.Model):
   
    name = models.CharField(max_length=50)
   
    description = models.TextField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name
   
class Exersice(models.Model):
    
    name = models.CharField(max_length=50)
    
    primary_muscle = models.CharField(choices=PrimaryMuscle.choices)
    
    secondry_muscle = models.ManyToManyField(SecondryMuscle, related_name='secondry_muscles',null=True , blank=True)
     
    equipment = models.ManyToManyField(Equipment,related_name='equipments',null=True , blank=True)
    
    difcullty = models.CharField(choices=Level.choices,null=True,blank=True)
    
    video = models.URLField(null=True , blank=True)
    

    def __str__(self):
        return f'-{self.name} -->> {self.primary_muscle} ->> {self.difcullty}'
    
class Split(models.Model):
    
    class Systems(models.TextChoices):
        
        PPL = 'Push Pull Leg' ,'Push Pull Leg'
         
        PRO_SPLIT = 'Pro Split' , 'Pro Split'
         
        ARNOLD_SPLIT = 'Arnold Split' , 'Arnold Split' 
        
        UPPER_LOWER = 'Upper & Lower' , 'Upper & Lower'
        
        INTIRIOR_EXTIRIOR = 'Intirior & Extirior'
        
        FULL_BODY = 'Full Body' , 'Full Body'
        
    split_type = models.CharField(choices=Systems.choices, max_length=50)
    
    description = models.TextField(max_length=400,null=True,blank=True)
    
    def __str__(self):
        return self.split_type
    

    
class ProgramTemlate(models.Model):
    
    name = models.CharField(max_length=50, help_text='Ex: Pro split Begainer,....')    
    
    split = models.ForeignKey(Split,on_delete=models.CASCADE,related_name='splits')
    
    level = models.CharField(choices=Level.choices)
    
    description = models.TextField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return f'{self.name}'
    
    

class ProgramDay(models.Model):
    
    program = models.ForeignKey(ProgramTemlate, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)

    order = models.PositiveIntegerField()
    
    class Meta:
        ordering = ["order"]
        
        unique_together = ["program", "order"]
        
    def __str__(self):
        return f'{self.name} -->> {self.program}'
        
class ProgramExersice(models.Model):
    
    slug = models.SlugField(null=True , blank=True , max_length=60)
    
    
    program_day = models.ForeignKey(ProgramDay,on_delete=models.CASCADE,related_name='exersices')
    
    exersice = models.ManyToManyField(Exersice,related_name='program_exersices')
    
    order = models.PositiveIntegerField()
    
    sets = models.PositiveIntegerField()
    
    min_reps = models.PositiveIntegerField()
    
    max_reps = models.PositiveIntegerField()
    
    rest_minutes = models.PositiveIntegerField()
    
    
    class Meta:
        ordering = ["order"]
        
        unique_together = ["program_day", "order"]
        
    def __str__(self):
        return f"{self.program_day} : {self.exersice}"