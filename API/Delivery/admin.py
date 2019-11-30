from django.contrib import admin
from .models import (Usuario, Restaurante, Classificacao_Usuario, Classificacao_Restaurante, 
    Fotos_Comida, Fotos_Restaurante, Ingredientes, Tipo, Tamanho, Codimentos, Codimentos_Restaurante,
    Pedido, Pedido_Restaurante, Comentario, Restaurante_Tag, Tags, Cardapio)

admin.site.register(Usuario)
admin.site.register(Restaurante)
admin.site.register(Classificacao_Restaurante)
admin.site.register(Classificacao_Usuario)
admin.site.register(Fotos_Comida)
admin.site.register(Fotos_Restaurante)
admin.site.register(Ingredientes)
admin.site.register(Tipo)
admin.site.register(Codimentos)
admin.site.register(Tamanho)
admin.site.register(Cardapio)
admin.site.register(Pedido)
admin.site.register(Pedido_Restaurante)
admin.site.register(Comentario)
admin.site.register(Restaurante_Tag)
admin.site.register(Tags)
admin.site.register(Codimentos_Restaurante)







