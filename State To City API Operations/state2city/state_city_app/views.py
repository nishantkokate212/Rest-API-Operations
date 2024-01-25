from django.shortcuts import render
from . serializers import State_district_city_Serializer,AllinOneSerializer
from .models import State
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class GetStatesData(APIView):                       #fetching all the data with multi serialzers
    def post(self,req,format=None):
        statedata=State.objects.all()
        serializer=State_district_city_Serializer(statedata,many=True)  
        if serializer:
            return Response(serializer.data)
        else:
            return Response({"msg":"invalid data"},status=status.HTTP_204_NO_CONTENT)

class Get_Filter_State_Data(APIView):   #Fetching specific state related data with multi serializers
    def post(self,req,format=None):
        data=req.data
        state_list=data.get("state_name")
        statedata=State.objects.filter(state_name__in=state_list)
        serializer=State_district_city_Serializer(statedata,many=True)
        if serializer:
             return Response(serializer.data)
            
        else:
            return Response({"msg":"invalid data"},status=status.HTTP_204_NO_CONTENT)
           
            
    


class GetStatesData_single_serializer(APIView):
    def post(self,req,format=None):
        statedata=State.objects.all()
        serializer=AllinOneSerializer(statedata,many=True)
        if serializer:
            return Response(serializer.data)
            
            
        else:
            return Response({"msg":"invalid data"},status=status.HTTP_204_NO_CONTENT)
            

class Get_Filter_State_Data_single_serializer(APIView):
    def post(self,req,format=None):
        data=req.data
        state_list=data.get("state_name")
        statedata=State.objects.filter(state_name__in=state_list)
        serializer=AllinOneSerializer(statedata,many=True)
        if serializer:
            return Response(serializer.data)
        else:
            return Response({"msg":"invalid data"},status=status.HTTP_204_NO_CONTENT)