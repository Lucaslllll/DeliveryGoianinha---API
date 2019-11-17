from django.conf.urls import url
from django.urls import include
from . import views
from django.urls import path


urlpatterns = [
	path('api/mensagem/<int:cliente>/<int:restaurante>', views.mensagem_lista, name='mensagem_lista'), 
	path('api/mensagem/', views.mensagem_lista, name='mensagem_lista'),   
    
]