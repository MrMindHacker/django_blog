from django.shortcuts import render
from django.http import HttpResponse
from . models import Car
from . serializers import carSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import json

#from django.views.decorators.cstf import cstf_exempt

# Create your views here.

class carList(APIView):
    lookup_field = 'name'
    serializer_class = carSerializer

    def get(self, request):
        cars = Car.objects.all()
        serializer = carSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = carSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
def get_car(request, car_name):
    if request.method == "GET":
        try:
            car = Car.objects.get(name=car_name)
            response = json.dumps([{ 'car': car.name, "Top Speed": car.top_speed}])
        except:
            response = json.dumps([{ 'Error': 'No Car With That Name..'}])
    return HttprResponse(response, content_type='text/json')
"""
