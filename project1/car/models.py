from django.db import models

# Create your models here.
class Car(models.Model):
    car_id=models.IntegerField(primary_key=True)
    car_brand=models.CharField(max_length=100)
    car_model=models.CharField(max_length=100)
    year=models.DateField()
    car_price=models.IntegerField()
    car_color=models.CharField(max_length=100)
    
