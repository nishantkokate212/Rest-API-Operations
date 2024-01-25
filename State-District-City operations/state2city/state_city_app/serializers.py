from rest_framework import serializers
from .models import *

class AllinOneSerializer(serializers.ModelSerializer):
    districts=serializers.SerializerMethodField('get_district_city')

    class Meta:
        model=State
        fields=('state_name','districts')

    def get_district_city(self,obj):
        state_id=obj.state_id
        districts_data=District.objects.filter(state=state_id).values('district_id','district_name')
        for d in districts_data:
            district_id=d.get('district_id')
            d['cities']=City.objects.filter(district=district_id).values('city_name')
        return districts_data