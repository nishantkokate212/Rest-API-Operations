from django.shortcuts import render
from .serializers import CityToStateSerializer,All_In_Single_Serial
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class GetCityData(APIView):
    def post(self,req):
        citydata=City.objects.all()
        serializer=CityToStateSerializer(citydata,many=True)
        return Response(serializer.data)
    
class GetFilterCityData(APIView):
    def post(self,req):
        data=req.data
        city_list=data.get('city_name')
        citydata=City.objects.filter(city_name__in=city_list)
        serializer=CityToStateSerializer(citydata,many=True)
        return Response(serializer.data)
    

#single serializers view below
    
class GetCityData_SS(APIView):
    def post(self,req):
        citydata=City.objects.all()
        serializer=All_In_Single_Serial(citydata,many=True)
        return Response(serializer.data)


class GetFilterCityData_SS(APIView):
    def post(self, request):
        data=request.data
        city_list=data.get('city_name')
        city_data = City.objects.filter(city_name__in=city_list)
        serializer = All_In_Single_Serial(city_data, many=True)
        return Response(serializer.data)
        
       
