from django.contrib import admin
from .models import Codigo

class CodigoAdmin(admin.ModelAdmin):
    readonly_fields = ('posting_date',)

admin.site.register(Codigo, CodigoAdmin)