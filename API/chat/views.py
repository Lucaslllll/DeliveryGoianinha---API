from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Mensagem
from .serializers import MensagemSerializer

@csrf_exempt
def mensagem_lista(request, cliente=None, restaurante=None):
  
    if request.method == 'GET':
        mensagens = Mensagem.objects.filter(cliente_id=cliente, restaurante_id=restaurante, lida=False)
        serializer = MensagemSerializer(mensagens, many=True, context={'request': request})
        for mensagem in mensagens:
            mensagem.lido = True
            mensagem.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MensagemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)