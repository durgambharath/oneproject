from django.db import models

#Create your models here.
class Menu(models.Model):

    Quaters_Place=models.CharField(max_length=30)
    Quaters_Number = models.CharField(max_length=30)
    Quaters_Type = models.CharField(max_length=30)
    Quaters_Description=models.CharField(max_length=30)
    Quaters_Date = models.CharField(max_length=30)
    Contract_Service_Number = models.CharField(primary_key=True,max_length=120)
    Electric_Meter_Number = models.CharField(max_length=20)



    def __str__(self):
        return self.Quaters_Place





