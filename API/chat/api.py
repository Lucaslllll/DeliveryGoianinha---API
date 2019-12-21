from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .models import Mensagem
from Delivery.models import Restaurante
from .serializers import MensagemSerializer, FiltrarMensagemSerializer


class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer

class PegarMensagem(generics.RetrieveAPIView):
    queryset = Mensagem.objects.all()
    serializer_class = FiltrarMensagemSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            try:
                restaurante = Restaurante.objects.get(pk=kwargs['restaurante'])
            except Restaurante.DoesNotExist:
                return Response("Restaurante não existente")

            try:
                user = User.objects.get(pk=kwargs['cliente'])
            except Restaurante.DoesNotExist:
                return Response("Cliente não existente")
        else:
            restaurante = None


        if restaurante == None:
            return Response("Sem dados")
        else:
            dic = {}; n = 0;

            for pk in Mensagem.objects.filter(restaurante=restaurante.pk, cliente=user.pk).values():
                dic[n] = pk['id']
                n += 1
            lista = [None]*len(dic); n = 0;

            # dic dentro da lista

            for i in dic.values():
                mensagem = Mensagem.objects.get(pk=i)


                # sempre colocar listas
                lista[n] = { 
                    'id': mensagem.id,
                    'cliente': mensagem.cliente.username,
                    'restaurante': mensagem.restaurante.nome,
                    'mensagem': mensagem.mensagem,
                    'hora_envio': mensagem.hora_envio,
                    'remetente': mensagem.remetente.nome,
                    'lida': mensagem.lida,
                }
                n += 1
        

            return Response({
                "restaurante": restaurante.nome,
                "conversas": lista
            })


class MensagensCliente(generics.RetrieveAPIView):
    queryset = Mensagem.objects.all()
    serializer_class = FiltrarMensagemSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            
            try:
                user = User.objects.get(pk=kwargs['cliente'])
            except Restaurante.DoesNotExist:
                return Response("Cliente não existente")
        else:
            user = None


        if user == None:
            return Response("Sem dados")
        else:
            dic = {}; n = 0;

            for pk in Mensagem.objects.filter(cliente=user.pk).values():
                dic[n] = pk['id']
                n += 1
            lista = [None]*len(dic); n = 0;

            # dic dentro da lista


            for i in dic.values():
                mensagem = Mensagem.objects.get(pk=i)


                # sempre colocar listas
                lista[n] = { 
                    'id': mensagem.id,
                    'cliente': mensagem.cliente.username,
                    'restaurante': mensagem.restaurante.nome,
                    'mensagem': mensagem.mensagem,
                    'hora_envio': mensagem.hora_envio,
                    'remetente': mensagem.remetente.nome,
                    'lida': mensagem.lida,
                }
                n += 1
            

            # recuperar nomes de restaurantes
            restaurantes = Restaurante.objects.all()
            nomes = [None]*len(restaurantes); index = 0;

            for i in restaurantes.values():
                for x in range(0, len(lista)):
                    if i['nome'] == lista[x]['restaurante']:
                        nomes[index] = i['nome']
                    

                    # print(nomes)
                index += 1
            # -------------------------------------------------- #

            dicReal = {}       
            for i in nomes:    
                # index = 0;
                for x in range(0, len(lista)):
                    if lista[x]['restaurante'] == i:
                        res = Restaurante.objects.get(nome=lista[x]['restaurante'])
                        msg = Mensagem.objects.filter(restaurante=res.pk, cliente=user.pk)
                        quantidade = len(msg)
                        dicReal[i+" quantidade de mensagens"] = len(msg)

                        # print("|||||||||||")      
                        # print(quantidade)
                        # print("|||||||||||")
                    # index += 1



            dic = {'restaurantes':nomes, 'mensagens': lista, 'total mensagens': dicReal}
            return Response(dic)


class MensagensRestaurante(generics.RetrieveAPIView):
    queryset = Mensagem.objects.all()
    serializer_class = FiltrarMensagemSerializer

    def retrieve(self, request, *args, **kwargs):
        if bool(self.get_queryset()):
            serializer = self.serializer_class(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            
            try:
                restaurante = Restaurante.objects.get(pk=kwargs['restaurante'])
            except Restaurante.DoesNotExist:
                return Response("Restaurante não existente")
        else:
            restaurante = None


        if restaurante == None:
            return Response("Sem dados")
        else:
            dic = {}; n = 0;

            for pk in Mensagem.objects.filter(restaurante=restaurante.pk).values():
                dic[n] = pk['id']
                n += 1
            lista = [None]*len(dic); n = 0;

            # dic dentro da lista


            for i in dic.values():
                mensagem = Mensagem.objects.get(pk=i)


                # sempre colocar listas
                lista[n] = { 
                    'id': mensagem.id,
                    'cliente': mensagem.cliente.username,
                    'restaurante': mensagem.restaurante.nome,
                    'mensagem': mensagem.mensagem,
                    'hora_envio': mensagem.hora_envio,
                    'remetente': mensagem.remetente.nome,
                    'lida': mensagem.lida,
                }
                n += 1
            

            # recuperar nomes de restaurantes
            user = User.objects.all()
            nomes = [None]*len(user); index = 0;

            for i in user.values():
                for x in range(0, len(lista)):
                    if i['username'] == lista[x]['cliente']:
                        nomes[index] = i['username']
                    

                    # print(nomes)
                index += 1
            # -------------------------------------------------- #

            dicReal = {}       
            for i in nomes:    
                # index = 0;
                for x in range(0, len(lista)):
                    if lista[x]['cliente'] == i:
                        u = User.objects.get(username=lista[x]['cliente'])
                        msg = Mensagem.objects.filter(restaurante=restaurante.pk, cliente=u.pk)
                        quantidade = len(msg)
                        dicReal[i+" quantidade de mensagens"] = len(msg)

                        # print("|||||||||||")      
                        # print(quantidade)
                        # print("|||||||||||")
                    # index += 1



            dic = {'cliente':nomes, 'mensagens': lista, 'total mensagens': dicReal}
            return Response(dic)