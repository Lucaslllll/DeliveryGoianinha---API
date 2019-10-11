from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_auth.serializers import UserDetailsSerializer



# serializer do usuario 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# serializer para registro
class RegisterSerializer(serializers.ModelSerializer):
    User._meta.get_field('email')._unique = True
    User._meta.get_field('username')._unique = True
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])

        return user

# serializer para autenticação
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user != None:
            user = authenticate(username=user.username, password=data['password'])
            if user and user.is_active:
                 return user
            raise serializers.ValidationError("Dados errados")
        else:
            raise serializers.ValidationError("Dados errados")


class VerifySerializer(serializers.Serializer):
    pk = serializers.CharField()
    token = serializers.CharField()
    
class LogoutSerializer(serializers.Serializer):
    pk = serializers.CharField()