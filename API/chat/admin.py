from django.contrib import admin
from .models import Mensagem, Remetente

# Register your models here.
admin.site.register(Mensagem)
admin.site.register(Remetente)