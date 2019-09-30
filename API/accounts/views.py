from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, permissions

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({

            'token': token.key,
        
        })


# receberá um token e id e irá pegar um token no db
class VerifyToken(generics.GenericAPIView):

	def post(self, request, *args, **kwargs):

		serializer = self.serializer_class(data=request.data, context={'request': request})