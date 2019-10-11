from rest_framework import generics, permissions
from rest_framework.response import Response
#from knox.models import AuthToken
from rest_framework.authtoken.models import Token
from .serializers import (UserSerializer, RegisterSerializer, LoginSerializer, 
                          VerifySerializer, LogoutSerializer)
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


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

        try:
            user_ = User.objects.get(username=user)
        except User.DoesNotExist:
            user_ = None

        if user_ != None:
            token = Token.objects.create(user=user_)
            return Response({

                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": token.key
            })
        else:
            return Response("email inválido")


    

# API para pegar user
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    



# receberá um token e id e irá pegar um token no db
class VerifyToken(generics.GenericAPIView):
    serializer_class = VerifySerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        pk = serializer.data['pk']
        token = serializer.data['token']
        token_f = Token.objects.filter(user=pk)
        token_ = get_object_or_404(token_f, user=pk)
        if token == token_.key:
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
        token = Token.objects.filter(user=pk)
        token_ = get_object_or_404(token, user=pk)
        
        token_.delete()
        return Response("Logout feito com sucesso!")
        
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