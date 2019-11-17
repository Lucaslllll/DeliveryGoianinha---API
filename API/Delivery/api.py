from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .serializers import (
    UserSerializer, UsuarioSerializer, RestauranteSerializer, FotosRestauranteSerializer, 
    ClassificacaoRestauranteSerializer, ClassificacaoRestauranteFNSerializer, 
    ClassificacaoUsuarioSerializer, ClassificacaoUsuarioFNSerializer, ComidaSerializer, IngredientesSerializer, 
    CodimentosSerializer, TamanhoSerializer, PedidoSerializer, PedidoRestauranteSerializer, 
    ComentarioSerializer, TagRestauranteSerializer, TagSerializer, TagRestauranteFiltrarSerializer, 
)
from .models import (Usuario, Restaurante, Classificacao_Usuario, Classificacao_Restaurante, 
                    Fotos_Comida, Fotos_Restaurante, Ingredientes, Tipo, Tamanho, Codimentos,
                    Pedido, Pedido_Restaurante, Comentario, Restaurante_Tag, Tags)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    lookup_field = 'slug'


# Classificacao restaurante

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

        if classificacao == None:
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


# Classificacao usuario

class ClassificacaoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = Classificacao_Usuario.objects.all()
    serializer_class = ClassificacaoUsuarioSerializer 

class ClassificacaoUsuarioFinal(generics.RetrieveAPIView):
    queryset = Classificacao_Usuario.objects.all()
    serializer_class = ClassificacaoUsuarioFNSerializer


    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)

            try:
                usuario = User.objects.get(pk=kwargs['pk'])
            except User.DoesNotExist:
                return Response("Não existe usuario")

            classificacao = Classificacao_Usuario.objects.filter(usuario=usuario.pk)
        else:
            classificacao = None

        if classificacao == None:
            return Response("Sem dados")
        else:
            media = 0
            
            cr = list(classificacao)
            
            n = 0
            for x in range(0, len(cr)):
                n += 1
                nota = cr[x].nota
                media += nota
            media /= n

            return Response({
                "usuário": usuario.username,
                "nota": media
            })


# comida

class ComidaViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = ComidaSerializer

class IngredientesViewSet(viewsets.ModelViewSet):
    queryset = Ingredientes.objects.all()
    serializer_class = IngredientesSerializer

class CodimentosViewSet(viewsets.ModelViewSet):
    queryset = Codimentos.objects.all()
    serializer_class = CodimentosSerializer

class TamanhoViewSet(viewsets.ModelViewSet):
    queryset = Tamanho.objects.all()
    serializer_class = TamanhoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoRestauranteViewSet(viewsets.ModelViewSet):
    queryset = Pedido_Restaurante.objects.all()
    serializer_class = PedidoRestauranteSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


# tag

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class TagRestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante_Tag.objects.all()
    serializer_class = TagRestauranteSerializer
        

class FiltrarTagRestaurante(generics.RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class= TagRestauranteFiltrarSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            try:
                tags = Tags.objects.get(nome=kwargs['nome'])
            except Tags.DoesNotExist:
                return Response("Tag não existente")
            
        else:
            classificacao = None

        if self.queryset == None:
            return Response("Sem dados")
        else:
            # print(restaurante_tag.restaurante_id)
            dic = {}; n = 0;

            for pk in Restaurante_Tag.objects.filter(tag=tags.pk).values():
                dic[n] = pk['restaurante_id']
                n += 1
            lista = [None]*len(dic); n = 0

            # dic dentro da lista
            for i in dic.values():
                lista[n] = { 
                    'id': Restaurante.objects.get(pk=i).id,
                    'nome': Restaurante.objects.get(pk=i).nome,
                    'descricao_breve': Restaurante.objects.get(pk=i).descricao_breve,
                    'slug': Restaurante.objects.get(pk=i).slug,
                    'status': Restaurante.objects.get(pk=i).status,
                }
                n += 1                   


            return Response({
                "restaurantes": lista
            })



    # def dados(self, *args, **kwargs):
    #     yield kwargs[]

class PegarPedidosRestaurante(generics.RetrieveAPIView):
    queryset = Pedido_Restaurante.objects.all()
    serializer_class= PedidoRestauranteSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            try:
                restaurante = Restaurante.objects.get(slug=kwargs['restaurante_slug'])
            except Restaurante.DoesNotExist:
                return Response("Restaurante não existente")
            
        else:
            restaurante = None

        if restaurante == None:
            return Response("Sem dados")
        else:
            # print(restaurante_tag.restaurante_id)
            dic = {}; n = 0;

            for pk in Pedido_Restaurante.objects.filter(restaurante=restaurante.pk).values():
                dic[n] = pk['pedido_id']
                n += 1
            lista = [None]*len(dic); n = 0

            # dic dentro da lista

            for i in dic.values():
                codimentos = []; index = 0;
                pedido = Pedido.objects.get(pk=i)

                for val in pedido.codimentos.values():
                    codimentos.append(val)
                    index += 1


                # sempre colocar listas
                lista[n] = { 
                    'id': Pedido.objects.get(pk=i).id,
                    'detalhes': Pedido.objects.get(pk=i).detalhes,
                    'nome': pedido.nome.nome,
                    'tamanho': pedido.tamanho.nome,
                    'unidades': Pedido.objects.get(pk=i).unidades,
                    'tempo': Pedido.objects.get(pk=i).tempo,
                    'codimentos': codimentos,
                    'cliente': pedido.cliente.pk,
                }
                n += 1      
                   

            return Response({
                "restaurante": restaurante.nome,
                "pedidos": lista
            })


class PegarComentariosRestaurante(generics.RetrieveAPIView):
    queryset = Pedido_Restaurante.objects.all()
    serializer_class= PedidoRestauranteSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            try:
                restaurante = Restaurante.objects.get(slug=kwargs['restaurante_slug'])
            except Restaurante.DoesNotExist:
                return Response("Restaurante não existente")
            
        else:
            restaurante = None

        if restaurante == None:
            return Response("Sem dados")
        else:
            # print(restaurante_tag.restaurante_id)
            dic = {}; n = 0;

            for pk in Comentario.objects.filter(restaurante=restaurante.pk).values():
                dic[n] = pk['id']
                n += 1
            lista = [None]*len(dic); n = 0;

            # dic dentro da lista

            for i in dic.values():
                comentario = Comentario.objects.get(pk=i)


                # sempre colocar listas
                lista[n] = { 
                    'id': comentario.id,
                    'restaurante': comentario.restaurante.nome,
                    'autor': comentario.autor.username,
                    'titulo': comentario.titulo,
                    'detalhes': comentario.descricao,
                    
                }
                n += 1      
                   

            return Response({
                "restaurante": restaurante.nome,
                "comentarios": lista
            })
