from rest_framework import serializers
from .models import *

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('state_name',)

class DistrictSerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = District
        fields = ('district_name', 'state')

class CityToStateSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()  # Change many=True to many=False

    class Meta:
        model = City
        fields = ('city_name', 'district')




class All_In_Single_Serial(serializers.ModelSerializer):
    districts = serializers.SerializerMethodField('get_districts')
    states = serializers.SerializerMethodField('get_states')

    class Meta:
        model = City
        fields = ('city_name', 'districts', 'states')

    def get_districts(self, obj):
        district = obj.district.district_name
        return district if district else None

    def get_states(self, obj):
        state = obj.district.state.state_name 
        return state if state else None
