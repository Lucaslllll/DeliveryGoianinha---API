from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
             return user
        raise serializers.ValidationError("Dados errados")


