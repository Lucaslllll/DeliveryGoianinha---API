from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


# API do registro
class RegistrarAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({

            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]

        }) 



# API do login
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({

            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]

        })

    def get_post_response_data(self, request, token, instance):
        UserSerializer = self.get_user_serializer_class()

        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token
        }
        if UserSerializer is not None:
            data["user"] = UserSerializer(
                request.user,
                context=self.get_context()
            ).data
        return data

# API para pegar user
class UserAPI(generics.RetrieveAPIView):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    

