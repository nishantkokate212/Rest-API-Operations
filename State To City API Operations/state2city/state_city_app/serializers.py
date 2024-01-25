from rest_framework import serializers
from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=('city_name',)

class DistrictSerializer(serializers.ModelSerializer):
    cities=CitySerializer(many=True,read_only=True)
    class Meta:
        model=District
        fields=('district_name','cities')

class State_district_city_Serializer(serializers.ModelSerializer):
    districts=DistrictSerializer(many=True,read_only=True)
    class Meta:
        model=State
        fields=("state_name","districts")


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