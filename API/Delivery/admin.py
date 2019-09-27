from django.contrib import admin
from .models import (Usuario, Restaurante, Classificacao_Usuario, Classificacao_Restaurante, 
					Fotos_Comida, Fotos_Restaurante, Ingredientes, Comida, Cardapio)

admin.site.register(Usuario)
admin.site.register(Restaurante)
admin.site.register(Classificacao_Restaurante)
admin.site.register(Classificacao_Usuario)
admin.site.register(Fotos_Comida)
admin.site.register(Fotos_Restaurante)
admin.site.register(Ingredientes)
admin.site.register(Comida)
admin.site.register(Cardapio)