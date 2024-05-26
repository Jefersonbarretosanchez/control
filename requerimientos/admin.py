from django.contrib import admin
from .models import Requerimientos

class RequerimientosAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Requerimientos"""
    list_display = ["ticket", 'requerimiento',
                    'fechacreacion', 'plataforma', 'estado']
    readonly_fields = ("fecharegistro", 'fecha_actualizacion')
    search_fields = ['ticket', 'requerimiento']
    list_filter = ['estado', 'plataforma']
    ordering = ['-fechacreacion', 'requerimiento']
    # ordering=['-id']
    list_display_links = ['ticket']
# Register your models here.

admin.site.register(Requerimientos, RequerimientosAdmin)
