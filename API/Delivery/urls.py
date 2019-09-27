from django.conf.urls import url
from rest_framework import routers
from . import api, views

router = routers.DefaultRouter()
router.register('api/user', api.UserViewSet, 'user')
router.register('api/usuario', api.UsuarioViewSet, 'usuario')
router.register('api/classficacao_usuario', api.ClassificacaoUsuarioViewSet, 'classficacao_usuario')
router.register('api/restaurante', api.RestauranteViewSet, 'restaurante')
router.register('api/classficacao_restaurante', api.ClassificacaoRestauranteViewSet, 'classificacao_restaurante')
router.register('api/comida', api.ComidaViewSet, 'comida')
router.register('api/ingredientes', api.IngredientesViewSet, 'ingredientes')
router.register('api/cardapio', api.CardapioViewSet, 'cardapio')
router.register('api/pedido', api.PedidoViewSet, 'pedido')
router.register('api/pedido_restaurante', api.PedidoRestauranteViewSet, 'pedido_restaurante')
router.register('api/comentario', api.ComentarioViewSet, 'comentario')



urlpatterns = router.urls


urlpatterns += [
	url(r'^api/foto_restaurante', views.FotosRestauranteCloud.as_view(), name='foto_restaurante'),	
	url(r'^api/foto_comida', views.FotosComidaCloud.as_view(), name='foto_comida')
]