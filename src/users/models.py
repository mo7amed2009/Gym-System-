from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import ( MaxLengthValidator,
                                   MaxValueValidator,
                                   MinLengthValidator,
                                   MinValueValidator)

from django.db.models.signals import post_save 
from django.dispatch import receiver
import datetime
# Create your models here.



class User(AbstractUser):
    """ To Custimize in User Model """
    class Role(models.TextChoices):
        ADMIN = 'Admin', 'Admin'
        COACH = 'Coach', 'Coach' 
        TRAINEE = 'Trainee', 'Trainee'  
    role = models.CharField(
        max_length=10, 
        choices=Role.choices, 
        default=Role.TRAINEE)
    email = models.EmailField(unique=True) # Email Field 
    
    USERNAME_FIELD = 'email' # To Sign Up With Email Field
    
    REQUIRED_FIELDS = ('username',) # To Required UserName Field
    
    def __str__(self):
        """ This Method To return Name """
        
        return self.username
    



class UserProfile(models.Model):
    """ This For Profile For Everyone User """
    class Activety(models.TextChoices):
        NO_EXERSICE = "1.2" , 'No Exersice'
        MIDDLE = "1.37" , "Exersice 1-3 days/week "
        HIGH_MIDDLE = "1.55" , "Exersice 3-5 days/week "
        HIGH = "1.72" , 'Exersice 6-7 days/week'
        PRO = "1.9" , 'Profishinal'
        
    class Gender(models.TextChoices):
        """ For Chosee Gender """
        MALE = 'Male' , 'Male'
        FEMALE = 'Female' , 'Female'
        
    last_name = models.CharField(max_length=50,null=True,blank=True)
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
        
    age = models.IntegerField(help_text='Smallest age 10 Years',null=True,blank=True)
    
    bio = models.TextField(validators=[MinLengthValidator(5),MaxLengthValidator(250)],null=True,blank=True)
    
    hight = models.DecimalField(max_digits=4,decimal_places=1,null=True,blank=True)
    
    weight = models.DecimalField(decimal_places=2,
                                 max_digits=4,null=True,blank=True)
    
    gender = models.CharField(choices=Gender.choices, max_length=50)
    
    activety = models.CharField(max_length=70 , choices=Activety.choices )
    
    
    @property
    def bmi(self):
        
        if not self.hight or not self.weight:
            return 0
        
        hight_meter = self.hight / 100
        
        if (self.weight / hight_meter ** 2) < 18.5:
            return "You have Thiny Body"
        
        elif (self.weight / hight_meter ** 2) >=  18.5 and (self.weight / hight_meter ** 2) <= 24.9:
            return 'You have a Normal Body'
        
        elif (self.weight / hight_meter ** 2) >=  25.0 and (self.weight / hight_meter ** 2) <= 30:
            return 'You have a Heavy Body'
        
        else:
            return 'You have a Very Heavy Body'
        
    @property    
    def bmr(self):
        
        if not self.weight or not self.hight or not self.age:
            return 0
        else:
            if self.gender == 'Male':
                return round((10 * float(self.weight)) + (6.25 * float(self.hight)) - (5 * self.age ) + 5,2)
        
            else :    
                return round((10 * float(self.weight)) + (6.25 * float(self.hight)) - (5 * self.age) - 161,2)
     
    @property   
    def tdee(self):   
        if not self.bmr or not self.activety:
            return 0
        
        return round(self.bmr * float(self.activety) ,2)
            
        
    def __str__(self):
        """ This Method To return Name """
        
        return self.user.username
    
    
    
class UserInfo(models.Model):
    """ This For Routine User """
    class ChoiceGoal(models.TextChoices):
        BULK = 'BULK' , 'BULK'
        CUT = "" , "CUT"
        MAINTAIN = "Stay same" , "Stay same" 
    
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='profile')
    
    goal = models.CharField(max_length=20, choices=ChoiceGoal.choices, null=True , blank=True)
    
    is_active = models.BooleanField(default=True)
    


    @property
    def target_goal(self):
        
        try:
            tdee = self.profile.tdee
            
            if self.goal == 'BULK':
                return round(tdee + 500 , 2)
            
            elif self.goal == 'CUT':
                return round(tdee - 300 , 2)
            else:
                return round(tdee, 2)
        except UserProfile.DoesNotExist:
            return 0.0

    @property
    def target_protein_g(self):
        if not self.target_goal :
            return 0
        
        presentage = 0.30 if self.goal == 'CUT' else 0.25
        
        result = round(float(self.target_goal )* presentage / 4 , 2)
    
        return result
     
    @property
    def target_fats_g(self):
        if not self.target_goal :
            return 0
        
        presentage = 0.25
        
        result = round(float(self.target_goal )* presentage  / 9 , 2 )
        
        return result
    
    @property
    def target_carbs_g(self):
        protein_calories = self.target_protein_g * 4
        
        fats_calories = self.target_fats_g * 9
        
        calories_without_carbs = protein_calories + fats_calories
        
        result = round((self.target_goal - calories_without_carbs) / 4 , 2)
        
        return result
        
    @property
    def target_creatine_g(self):
        
        if not self.profile.weight:
            return 0
        
        result = round(float(self.profile.weight) * 0.03 , 1)
        
        return result
        
    def __str__(self):
        """ This Method To return Name """
        
        return self.profile.user.username
    
    
    
@receiver(post_save,sender=User)    
def create_profile(sender,instance,created, **kw):
    """ This Function Signal To create Profile To EveryOne User """
    
    if created:
        UserProfile.objects.create(
            user = instance
        )
  
@receiver(post_save, sender=UserProfile)      
def create_user_info(sender,instance,created,**kw):
    """ This Function Signal To create Profile Info  To EveryOne User """
    
    if created:
        UserInfo.objects.create(
            profile=instance
        )