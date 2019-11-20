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

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from accounts.serializers import UserSerializer
from django.contrib.auth.models import User

class UserCreate(APIView):
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

