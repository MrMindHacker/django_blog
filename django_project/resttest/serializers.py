from rest_framework import serializers
from . models import Car
from django.contrib.auth.models import User

class carSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
