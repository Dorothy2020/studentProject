# from schoolsystem.schoolsystem.settings import LANGUAGE_CODE
from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=15)
    age=models.PositiveBigIntegerField()
    date_of_birth=models.DateField()
    Email_address=models.EmailField()
    Student_id=models.CharField(max_length=15)
    Date_of_enrollment=models.DateField()
    County=models.CharField(max_length=12) 
    Medical_report=models.FileField()
    Course_name=models.CharField(max_length=12)
    Roll_number=models.CharField(max_length=15)
    Profile = models.ImageField(upload_to ='Profile/% Y/% m/% d/')
    GENDER_CHOICES=(
        (u'M',u'Male'),
        (u'F',u'Female'),
        (u'O',u'Other'),
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)


    LANGUAGE_CHOICES =(
         (u'En',u'English'),
        (u'S',u'Swahili'),
        (u'K',u'KinyaRwanda'),
    )

    language=models.CharField(max_length=6,choices=LANGUAGE_CHOICES)



 
    
     
    
                        
        
    
    

    
