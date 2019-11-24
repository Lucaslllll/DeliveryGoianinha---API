from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import (UserSerializer, UserFNSerializer, RegisterSerializer, LoginSerializer, 
                          VerifySerializer, LogoutSerializer, ResetSerializer)
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core import mail

from rest_framework import viewsets, permissions, generics
from django.template.loader import render_to_string
from .utils import email_client
from .tokens import account_activation_token



# API do registro
class RegistrarAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = Token.objects.create(user=user)
        return Response({

            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key

        }) 



# API do login
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data

        user_ = User.objects.get(username=user)
        
        try: 
            token = Token.objects.create(user=user_)
        except: 
            return Response({
                "id": user_.id,
                "estado": False
            })

        return Response({

            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key,
            "estado": True
        })


    

# API para pegar user
class UserAPI(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data

        return Response({
            "id": user.pk,
            "username": user.username,
            "email": user.email

        })
    



# receberá um token e id e irá pegar um token no db
class VerifyToken(generics.GenericAPIView):
    serializer_class = VerifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        token = request.data['token']
        get_token = serializer.validated_data

        if get_token == token:
            return Response(True,)
        else:
            return Response(False,)

# receberá somente um id
class Logout(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        pk = serializer.data['pk']

        try:
            token = Token.objects.get(user=pk)
        except Token.DoesNotExist:
            token = None

        if token == None:
            return Response("Logout já feito!")
        else:    
            token.delete()
            return Response("Logout feito com sucesso!")
        

class ResetPasswordAPI(generics.GenericAPIView):
    serializer_class = ResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data
        
        user = User.objects.get(pk=request.data['pk'])
        user.set_password(password)
        user.save()
        
        return Response({

            "user": UserSerializer(user, context=self.get_serializer_context()).data,

        })




class EmailList(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        email_client(request, user)
        return Response("Email enviado")
        

class EmailConfirme(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserFNSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)

            try:
                user = User.objects.get(pk=kwargs['pk'])
            except User.DoesNotExist:
                return Response("Não existe usuário")
            

            if user is not None and account_activation_token.check_token(user, kwargs['token']):
                return Response(True,)
            else:
                return Response(False,)

# def get_post_response_data(self, request, token, instance):
#         UserSerializer = self.get_user_serializer_class()

#         data = {
#             'expiry': self.format_expiry_datetime(instance.expiry),
#             'token': token
#         }
#         if UserSerializer is not None:
#             data["user"] = UserSerializer(
#                 request.user,
#                 context=self.get_context()
#             ).data
#         return data