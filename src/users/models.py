from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import ( MaxLengthValidator,
                                   MaxValueValidator,
                                   MinLengthValidator,
                                   MinValueValidator)

from django.db.models.signals import post_save 
from django.dispatch import receiver
# Create your models here.



class User(AbstractUser):
    """ To Custimize in User Model """
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        COACH = 'COACH', 'Coach'
        TRAINEE = 'TRAINEE', 'Trainee'  
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
    class Gender(models.TextChoices):
        """ For Chosee Gender """
        MALE = 'Male' , 'Male'
        FEMALE = 'Female' , 'Female'
        OTHER = 'Other' , 'Other'
        
    last_name = models.CharField(max_length=50,null=True,blank=True)
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
        
    age = models.IntegerField(validators=[MinValueValidator(2),MaxValueValidator(2)],
                              help_text='Smallest age 10 Years',null=True,blank=True)
    
    bio = models.TextField(validators=[MinLengthValidator(5),MaxLengthValidator(250)],null=True,blank=True)
    
    tall = models.DecimalField(max_digits=3,decimal_places=2,null=True,blank=True)
    
    weight = models.DecimalField(validators=[MaxValueValidator(4),MinValueValidator(2)],
                                 decimal_places=2,null=True,blank=True,
                                 max_digits=4)
    
    gender = models.CharField(choices=Gender,default=Gender.OTHER)
    
    
    def __str__(self):
        """ This Method To return Name """
        
        return self.user.username
    
    
    
class UserInfo(models.Model):
    """ This For Routine User """
    
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='profile')
    
    day_of_exrsice = models.IntegerField(help_text="days of your exrsice in weak"
                                         ,null=True,blank=True)
    
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