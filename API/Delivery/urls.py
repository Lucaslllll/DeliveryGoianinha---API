from django.conf.urls import url
from django.urls import path
from rest_framework import routers
from . import api, views

router = routers.DefaultRouter()
# router.register('api/user', api.UserViewSet, 'user')
# router.register('api/usuario', api.UsuarioViewSet, 'usuario')
router.register('api/classificacao_usuario', api.ClassificacaoUsuarioViewSet, 'classficacao_usuario')
router.register('api/restaurante', api.RestauranteViewSet, 'restaurante')
router.register('api/classificacao_restaurante', api.ClassificacaoRestauranteViewSet, 'classificacao_restaurante')
router.register('api/comida', api.ComidaViewSet, 'comida')
router.register('api/ingredientes', api.IngredientesViewSet, 'ingredientes')
router.register('api/cardapio', api.CardapioViewSet, 'cardapio')
router.register('api/pedido', api.PedidoViewSet, 'pedido')
router.register('api/pedido_restaurante', api.PedidoRestauranteViewSet, 'pedido_restaurante')
router.register('api/comentario', api.ComentarioViewSet, 'comentario')
router.register('api/tags', api.TagViewSet, 'tags')
router.register('api/tag_restaurante', api.TagRestauranteViewSet, 'tag_restaurante')


urlpatterns = router.urls


urlpatterns += [
	# retrieve
	path('api/classificacao_restaurante_final/<str:restaurante_slug>', api.ClassificacaoRestauranteFinal.as_view(), name='classificacao_restaurante_final'),
	path('api/filtrar_restaurante/<str:nome>', api.FiltrarTagRestaurante.as_view(), name='tag_filtro'),
	
	path('api/foto_restaurante', views.FotosRestauranteCloud.as_view(), name='foto_restaurante'),	
	path('api/foto_comida', views.FotosComidaCloud.as_view(), name='foto_comida')
]