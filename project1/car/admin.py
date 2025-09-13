from django.contrib import admin
from .models import Car
# Register your models here.
admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):
    list_display=('car_id','car_brand','car_model','year','car_price','car_color')