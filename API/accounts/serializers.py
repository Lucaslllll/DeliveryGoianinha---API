from rest_framework import serializers
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_auth.serializers import UserDetailsSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from .models import Codigo
from .backends import EmailAuthBackend


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

class RegisterEmailSerializer(serializers.ModelSerializer):
    User._meta.get_field('email')._unique = True
    class Meta:
        model = User
        fields = ('email',)
        extra_kwargs = {'password': {'write_only': True}}

    # parte abaixo não usada
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'], is_active=False)

        return user

    # def validate(self, data):



# serializer para registro
class RegisterConfirmeSerializer(serializers.Serializer):
    codigo = serializers.CharField()

    def validate(self, data):
        codigo = data['codigo']

        try:
            codigo = Codigo.objects.get(code=codigo)
        except Codigo.DoesNotExist:
            codigo = None

        if codigo == None:
            raise serializers.ValidationError("Código incorreto")
        else:
            return codigo
        

class RegisterSerializer(serializers.ModelSerializer):
    User._meta.get_field('username')._unique = False
    codigo = serializers.CharField()
    class Meta:
        model = User
        fields = ('id', 'codigo', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'],
                                        is_active=True)

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
            users = EmailAuthBackend.authenticate(self, username=email, password=data['password'])
            if users and user.is_active:
                # print(users.email)
                return users.email
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
        

