from django.conf.urls import url
from django.urls import include
from . import views, api
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/mensagem', api.MensagemViewSet, 'mensagem_lista')


urlpatterns = router.urls


urlpatterns += [
	path('api/filtrar_mensagem/<int:cliente>/<int:restaurante>', api.PegarMensagem.as_view(), name='filtrar_mensagem'), 
	
	path('api/mensagens_cliente/<int:cliente>', api.MensagensCliente.as_view(), name='mensagens_cliente'),
	path('api/mensagens_restaurante/<int:restaurante>', api.MensagensRestaurante.as_view(), name='mensagens_restaurante'),
]