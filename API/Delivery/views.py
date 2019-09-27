from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FotosRestauranteSerializer, FotosComidaSerializer
from .models import Fotos_Restaurante, Fotos_Comida, Comida
from cloudinary.templatetags import cloudinary
import cloudinary.uploader


class FotosRestauranteCloud(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = FotosRestauranteSerializer
    def get(self, request, format=None):
        fotos = Fotos_Restaurante.objects.all()
        serializer = FotosRestauranteSerializer(fotos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FotosComidaCloud(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = FotosComidaSerializer
    def get(self, request, format=None):
        fotos = Fotos_Comida.objects.all()
        serializer = FotosComidaSerializer(fotos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

