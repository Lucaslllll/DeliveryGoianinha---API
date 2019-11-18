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
	
]