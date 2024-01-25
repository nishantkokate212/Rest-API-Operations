from django.shortcuts import render
from . serializers import State_district_city_Serializer,AllinOneSerializer
from .models import State
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class GetStatesData_single_serializer(APIView):  # all state data
    def get(self,req,format=None):
        statedata=State.objects.all()
        serializer=AllinOneSerializer(statedata,many=True)
        if serializer:
            return Response(serializer.data)
            
            
        else:
            return Response({"msg":"invalid data"},status=status.HTTP_204_NO_CONTENT)
            

class Get_Filter_State_Data_single_serializer(APIView): #specific state data
    def get(self,req,format=None):
        data=req.data
        state_list=data.get("state_name")
        statedata=State.objects.filter(state_name__in=state_list)
        serializer=AllinOneSerializer(statedata,many=True)
        if serializer:
            return Response(serializer.data)
        else:
            return Response({"msg":"invalid data"},status=status.HTTP_204_NO_CONTENT)