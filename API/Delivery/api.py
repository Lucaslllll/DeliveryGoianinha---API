from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .serializers import (
    UserSerializer, UsuarioSerializer, UsuarioFNSerializer, RestauranteSerializer, RestauranteFNSerializer, FotosRestauranteSerializer, 
    ClassificacaoRestauranteSerializer, ClassificacaoRestauranteFNSerializer, 
    ClassificacaoUsuarioSerializer, ClassificacaoUsuarioFNSerializer, ComidaSerializer, IngredientesSerializer, 
    CodimentosSerializer, CodimentosRestauranteSerializer, TamanhoSerializer, PedidoSerializer, 
    PedidoRestauranteSerializer, ComentarioSerializer, TagRestauranteSerializer, TagSerializer,
    TagRestauranteFiltrarSerializer, CardapioSerializer,FiltrarComentarioSerializer, 
    FiltrarCardapioSerializer, CodimentosRestauranteFNSerializer, CorSerializer, TagComidaSerializer,
    TagComidaFiltrarSerializer
)
from .models import (Usuario, Restaurante, Classificacao_Usuario, Classificacao_Restaurante, 
                    Fotos_Comida, Fotos_Restaurante, Ingredientes, Tipo, Tamanho, Codimentos,
                    Codimentos_Restaurante, Pedido, Pedido_Restaurante, Comentario, Restaurante_Tag,
                    Tags, Cardapio, Cor, Comida_Tag)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

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

class CodimentosRestauranteViewSet(viewsets.ModelViewSet):
    queryset = Codimentos_Restaurante.objects.all()
    serializer_class = CodimentosRestauranteSerializer

class TamanhoViewSet(viewsets.ModelViewSet):
    queryset = Tamanho.objects.all()
    serializer_class = TamanhoSerializer

class CorViewSet(viewsets.ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoRestauranteViewSet(viewsets.ModelViewSet):
    queryset = Pedido_Restaurante.objects.all()
    serializer_class = PedidoRestauranteSerializer

class CardapioViewSet(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer

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
                    'cor': Restaurante.objects.get(pk=i).cor.nome,
                    'foto': Restaurante.objects.get(pk=i).foto.url,
                }
                n += 1                   


            return Response({
                "restaurantes": lista
            })


class FiltrarTagComida(generics.RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class= TagComidaFiltrarSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            try:
                tags = Tags.objects.get(nome=kwargs['nome'])
            except Tags.DoesNotExist:
                return Response("Tag não existente")
            
        else:
            tags = None

        if tags == None:
            return Response("Sem dados")
        else:
            # print(restaurante_tag.restaurante_id)
            dic = {}; n = 0;

            for pk in Comida_Tag.objects.filter(tag=tags.pk).values():
                dic[n] = pk['cardapio_id']
                n += 1
            lista = [None]*len(dic); n = 0

            # dic dentro da lista
            for i in dic.values():
                lista[n] = { 
                    'id': Cardapio.objects.get(pk=i).id,
                    'restaurante': Cardapio.objects.get(pk=i).restaurante.nome,
                    'nome': Cardapio.objects.get(pk=i).nome,
                    'preco': Cardapio.objects.get(pk=i).preco,
                    'quantidade': Cardapio.objects.get(pk=i).quantidade,
                    'destaque': Cardapio.objects.get(pk=i).destaque,
                    'foto': Cardapio.objects.get(pk=i).foto.url,
                }
                n += 1                   


            return Response({
                "comidas": lista
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

class PegarCodimentosRestaurante(generics.RetrieveAPIView):
    queryset = Codimentos_Restaurante.objects.all()
    serializer_class = CodimentosRestauranteFNSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)

            try:
                restaurante = Restaurante.objects.get(slug=kwargs['restaurante_slug'])
            except Restaurante.DoesNotExist:
                restaurante = None

            codimentos_restaurante = Codimentos_Restaurante.objects.filter(restaurante=restaurante.pk)
            
        else:
            restaurante = None

        if restaurante == None:
            return Response("Sem dados")
        else:
            # print(restaurante_tag.restaurante_id)
            dic = {}; n = 0;

            for pk in codimentos_restaurante.values():
                dic[n] = pk['id']
                n += 1
            lista = [None]*len(dic); n = 0;

            # dic dentro da lista

            for i in dic.values():
                codimentos = Codimentos.objects.get(pk=i)


                # sempre colocar listas
                lista[n] = { 
                    'id': codimentos.id,
                    'nome': codimentos.nome,
                    'preco': codimentos.preco,
                }
                n += 1      
                   

            return Response({
                "restaurante": restaurante.nome,
                "codimentos": lista
            })


class PegarComentariosRestaurante(generics.RetrieveAPIView):
    queryset = Comentario.objects.all()
    serializer_class = FiltrarComentarioSerializer

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
                    'id_autor': comentario.autor.id,
                    'autor': comentario.autor.username,
                    'titulo': comentario.titulo,
                    'detalhes': comentario.descricao,
                    
                }
                n += 1      
                   

            return Response({
                "restaurante": restaurante.nome,
                "comentarios": lista
            })

class PegarCardapioRestaurante(generics.RetrieveAPIView):
    queryset = Cardapio.objects.all()
    serializer_class = FiltrarCardapioSerializer

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

            for pk in Cardapio.objects.filter(restaurante=restaurante.pk).values():
                dic[n] = pk['id']
                n += 1
            lista = [None]*len(dic); n = 0;

            # dic dentro da lista

            for i in dic.values():
                cardapio = Cardapio.objects.get(pk=i)


                # sempre colocar listas
                lista[n] = { 
                    'id': cardapio.id,
                    'restaurante': cardapio.restaurante.nome,
                    'nome': cardapio.nome,
                    'preco': cardapio.preco,
                    'quantidade': cardapio.quantidade,
                    'foto': cardapio.foto.url
                }
                n += 1      

            return Response({
                "restaurante": restaurante.nome,
                "cardapio": lista
            })

class PegarFotoUser(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioFNSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            try:
                user = User.objects.get(pk=kwargs['pk'])
            except User.DoesNotExist:
                return Response("User não existente")
            
        else:
            user = None

        if user == None:
            return Response("Sem dados")
        else:
            try:
                usuario = Usuario.objects.get(user=user.pk)
            except Usuario.DoesNotExist:
                return Response("Usuário não tem foto ou não existe")

            return Response({
                "id": user.id,
                "foto": usuario.foto.url,
            })

class Buscar(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioFNSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            
            restaurante = Restaurante.objects.filter(nome__icontains=kwargs['nome'])
            cardapio = Cardapio.objects.filter(nome__icontains=kwargs['nome'])
            confirme = True

        else:
            confirme = None

        if confirme == None:
            return Response("Sem dados")
        else:
            dic1 = {}; n = 0;
            for pk in cardapio.values():
                dic1[n] = pk['id']
                n += 1
            lista1 = [None]*len(dic1); n = 0;

            for i in dic1.values():
                cardapio = Cardapio.objects.get(pk=i)


                lista1[n] = { 
                    'id': cardapio.id,
                    'restaurante': cardapio.restaurante.nome,
                    'nome': cardapio.nome,
                    'preco': cardapio.preco,
                    'quantidade': cardapio.quantidade,
                    'foto': cardapio.foto.url
                }
                n += 1



            dic2 = {}; n = 0;
            for pk in restaurante.values():
                dic2[n] = pk['id']
                n += 1
            lista2 = [None]*len(dic2); n = 0;

            for i in dic2.values():

                lista2[n] = { 
                    'id': Restaurante.objects.get(pk=i).id,
                    'nome': Restaurante.objects.get(pk=i).nome,
                    'descricao_breve': Restaurante.objects.get(pk=i).descricao_breve,
                    'slug': Restaurante.objects.get(pk=i).slug,
                    'cor': Restaurante.objects.get(pk=i).cor.nome,
                    'status': Restaurante.objects.get(pk=i).status,
                    'foto': Restaurante.objects.get(pk=i).foto.url,
                }
                n += 1

            return Response({
                "restaurante": lista2,
                "cardapio": lista1
            })


class PegarDestaques(generics.RetrieveAPIView):
    queryset = Cardapio.objects.all()
    serializer_class = FiltrarCardapioSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            
            restaurante = Restaurante.objects.get(slug__contains=kwargs['restaurante_slug'])
            cardapio = Cardapio.objects.filter(restaurante=restaurante.pk, destaque=True)
        else:
            cardapio = None

        if cardapio == None:
            return Response("Não há destaques nesse restaurante")
        else:
            dic = {}; n = 0;
            for pk in cardapio.values():
                dic[n] = pk['id']
                n += 1
            lista = [None]*len(dic); n = 0;

            for i in dic.values():
                cardapio = Cardapio.objects.get(pk=i)


                lista[n] = { 
                    'id': cardapio.id,
                    'restaurante': cardapio.restaurante.nome,
                    'nome': cardapio.nome,
                    'preco': cardapio.preco,
                    'quantidade': cardapio.quantidade,
                    'foto': cardapio.foto.url
                }
                n += 1

            dic = {'restaurantes': restaurante.nome, 'cardapios': lista}
            return Response(dic)