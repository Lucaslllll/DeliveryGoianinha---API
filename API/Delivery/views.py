from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FotosRestauranteSerializer, FotosComidaSerializer
from .models import Fotos_Restaurante, Fotos_Comida, Comida
from cloudinary.templatetags import cloudinary
import cloudinary.uploader
from rest_framework import viewsets, permissions, generics
from .models import Fotos_Restaurante


class FotosRestauranteCloud(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = FotosRestauranteSerializer
    queryset = Fotos_Restaurante.objects.all()

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

class FotosRestauranteCloudUD(generics.RetrieveAPIView):
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Fotos_Restaurante.objects.all()
    serializer_class = FotosRestauranteSerializer


    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)

        try:
            foto = Fotos_Restaurante.objects.get(pk=kwargs['pk'])
        except Fotos_Restaurante.DoesNotExist:
            return Response("Não existe foto")

        return Response({
            "restaurante": foto.restaurante.id,
            "foto": foto.foto.url
            })


    def put(self, request, pk, format=None):
        fotos = Fotos_Restaurante.objects.get(pk=pk)
        cloudinary.uploader.destroy(fotos.foto.public_id)
        serializer = self.serializer_class(fotos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        try:
            fotos = Fotos_Restaurante.objects.get(pk=pk)
            cloudinary.uploader.destroy(fotos.foto.public_id)
            fotos.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as message:
            return Response(status=status.HTTP_404_NOT_FOUND)



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


class FotosComidaCloudUD(generics.RetrieveAPIView):
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Fotos_Comida.objects.all()
    serializer_class = FotosComidaSerializer


    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)

        try:
            foto = Fotos_Comida.objects.get(pk=kwargs['pk'])
        except Fotos_Comida.DoesNotExist:
            return Response("Não existe foto")

        return Response({
            "comida": foto.comida.id,
            "foto": foto.foto.url
            })


    def put(self, request, pk, format=None):
        fotos = Fotos_Comida.objects.get(pk=pk)
        cloudinary.uploader.destroy(fotos.foto.public_id)
        serializer = self.serializer_class(fotos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        try:
            fotos = Fotos_Comida.objects.get(pk=pk)
            cloudinary.uploader.destroy(fotos.foto.public_id)
            fotos.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as message:
            return Response(status=status.HTTP_404_NOT_FOUND)

