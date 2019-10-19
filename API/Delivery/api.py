from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .serializers import (UserSerializer, UsuarioSerializer, RestauranteSerializer, FotosRestauranteSerializer, 
						 ClassificacaoRestauranteSerializer, ClassificacaoUsuarioSerializer, ComidaSerializer, IngredientesSerializer,
                         CardapioSerializer, PedidoSerializer, PedidoRestauranteSerializer, 
                         ComentarioSerializer)
from .models import (Usuario, Restaurante, Classificacao_Usuario, Classificacao_Restaurante, 
                    Fotos_Comida, Fotos_Restaurante, Ingredientes, Comida, Cardapio,
                    Pedido, Pedido_Restaurante, Comentario)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     permissions_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = UserSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class UsuarioViewSet(viewsets.ModelViewSet):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer


class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    lookup_field = 'slug'

class ClassificacaoRestauranteViewSet(viewsets.ModelViewSet):
    queryset = Classificacao_Restaurante.objects.all()
    serializer_class = ClassificacaoRestauranteSerializer


class ClassificacaoRestauranteFinal(generics.RetrieveAPIView):
    queryset = Classificacao_Restaurante.objects.all()
    serializer_class = ClassificacaoRestauranteSerializer


    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            restaurante = Restaurante.objects.get(nome=kwargs['restaurante'])
            classificacao = Classificacao_Restaurante.objects.filter(restaurante=restaurante.pk)
        else:
            classificacao = None

        if self.queryset == None:
            return Response("Sem dados")
        else:
            media = 0
            # list to use len()
            cr = list(classificacao)
    
            for x in range(0, len(cr)):
                nota = cr[x].nota
                media += nota
            media /= 5

            return Response({
                "restaurante": restaurante.nome,
                "nota": media
            })

class ClassificacaoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = Classificacao_Usuario.objects.all()
    serializer_class = ClassificacaoUsuarioSerializer 

class ComidaViewSet(viewsets.ModelViewSet):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer

class IngredientesViewSet(viewsets.ModelViewSet):
    queryset = Ingredientes.objects.all()
    serializer_class = IngredientesSerializer

class CardapioViewSet(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoRestauranteViewSet(viewsets.ModelViewSet):
    queryset = Pedido_Restaurante.objects.all()
    serializer_class = PedidoRestauranteSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

