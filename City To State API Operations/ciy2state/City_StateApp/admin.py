from django.contrib import admin
from .models import *
# Register your models here.

class StateAdmin(admin.ModelAdmin):
    list_display=['state_id','state_name']

class DistrictAdmin(admin.ModelAdmin):
    list_display=['district_id','district_name','state']

class CityAdmin(admin.ModelAdmin):
    list_display=['city_id','city_name','district']

admin.site.register(State,StateAdmin)
admin.site.register(District,DistrictAdmin)
admin.site.register(City,CityAdmin)

