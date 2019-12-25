from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_auth.serializers import UserDetailsSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from .models import Codigo



class CodigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codigo
        fields = '__all__'


# serializer do usuario 
class UserSerializer(serializers.Serializer):
    pk = serializers.CharField()

    def validate(self, validated_data):
        try:
            user = User.objects.get(pk=validated_data['pk'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuário não existe")

        return user

class UserFNSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', )

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

class VerifyLogon(serializers.Serializer):
    pk = serializers.CharField()


class VerifySerializer(serializers.Serializer):
    pk = serializers.CharField()
    token = serializers.CharField()
    
    def validate(self, data):
        pk = data['pk']
        token = data['token']

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            user = None

        if user == None:
            raise serializers.ValidationError("Usuário não existe")
        else:
            try:
                get_token = Token.objects.get(user=user.pk)
            except Token.DoesNotExist:
                get_token = None

            if get_token == None:
                raise serializers.ValidationError("Token não existe")
            else:
                return get_token.key



class LogoutSerializer(serializers.Serializer):
    pk = serializers.CharField()

class ResetSerializer(serializers.Serializer):
    pk = serializers.CharField()    
    atual_password = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    
    def validate(self, data):
        pk = data['pk']
        atual_password = data['atual_password']
        password1 = data['password1']
        password2 = data['password2']
        
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            user = None

        if user == None:
            raise serializers.ValidationError("Usuário não existe")
        else:
            confirmacao = check_password(atual_password, user.password)
            if confirmacao == True:    
                if password1 == password2:
                    return password1
                else:
                    raise serializers.ValidationError("Senhas diferentes")
            else:
                raise serializers.ValidationError("Senha atual incorreta")


class ChangePasswordSerializer(serializers.Serializer):
    pk = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        pk = data['pk']
        password1 = data['password1']
        password2 = data['password2']

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            user = None

        if user == None:
            raise serializers.ValidationError("Usuário não existe")
        else:
            if password1 == password2:
                return password1
            else:
                raise serializers.ValidationError("Senhas diferentes")
        

