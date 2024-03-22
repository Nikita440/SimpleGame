from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import UserInfo

from rest_framework.serializers import ModelSerializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            
            

        )
        return user


class SerializerForUserInfo(ModelSerializer):
    class Meta:
        model = UserInfo 
        fields = '__all__'



class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class TokenResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
    custom_data = serializers.DictField()

class Serializename(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['name']
