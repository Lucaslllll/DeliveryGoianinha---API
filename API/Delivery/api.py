from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .serializers import (UserSerializer, UsuarioSerializer, RestauranteSerializer, FotosRestauranteSerializer, 
						 ClassificacaoRestauranteSerializer, ClassificacaoRestauranteFNSerializer, 
                         ClassificacaoUsuarioSerializer, ComidaSerializer, IngredientesSerializer, 
                         CardapioSerializer, PedidoSerializer, PedidoRestauranteSerializer, 
                         ComentarioSerializer, TagRestauranteSerializer, TagSerializer)
from .models import (Usuario, Restaurante, Classificacao_Usuario, Classificacao_Restaurante, 
                    Fotos_Comida, Fotos_Restaurante, Ingredientes, Comida, Cardapio,
                    Pedido, Pedido_Restaurante, Comentario, Restaurante_Tag, Tags)


class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    lookup_field = 'slug'

class ClassificacaoRestauranteViewSet(viewsets.ModelViewSet):
    queryset = Classificacao_Restaurante.objects.all()
    serializer_class = ClassificacaoRestauranteSerializer


class ClassificacaoRestauranteFinal(generics.RetrieveAPIView):
    queryset = Classificacao_Restaurante.objects.all()
    serializer_class = ClassificacaoRestauranteFNSerializer


    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)

            try:
                restaurante = Restaurante.objects.get(slug=kwargs['restaurante_slug'])
            except Restaurante.DoesNotExist:
                return Response("Não existe restaurante")

            classificacao = Classificacao_Restaurante.objects.filter(restaurante=restaurante.pk)
        else:
            classificacao = None

        if self.queryset == None:
            return Response("Sem dados")
        else:
            media = 0
            # list to use len()
            cr = list(classificacao)
            
            n = 0 
            for x in range(0, len(cr)):
                n += 1
                nota = cr[x].nota
                media += nota
            media /= n

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

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class TagRestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante_Tag.objects.all()
    serializer_class = TagRestauranteSerializer
        
class FiltrarTagRestaurante(generics.RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class= TagRestauranteSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            tags = Tags.objects.get(nome=kwargs['nome'])
            restaurante_tag = Restaurante_Tag.objects.filter(tag=tags.pk)
            restaurantes = Restaurante.objects.filter(pk=restaurante_tag.pk)

        else:
            classificacao = None

        if self.queryset == None:
            return Response("Sem dados")
        else:
            dic = {}
            for x in restaurantes.nome:
                dic["restaurantes"]: restaurantes.nome
            return Response({
                "restaurantes": dic
                })