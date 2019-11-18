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
                "cardapio": lista
            })
