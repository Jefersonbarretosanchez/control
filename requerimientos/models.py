"""Importa modelos"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Requerimientos(models.Model):
    """Class representing a requerimiento"""
    ticket=models.CharField(max_length=100,verbose_name="# Ticket")
    requerimiento=models.CharField(max_length=100, blank=True, verbose_name="Nombre Requerimientos")
    fechacreacion=models.DateField(blank=False, verbose_name="Fecha Creación")
    mediocarga=models.CharField(max_length=100, blank=True, verbose_name="Medio Carga")
    plataforma=models.CharField(max_length=100, blank=True, verbose_name="Plataforma")
    estado=models.CharField(max_length=100, blank=True, verbose_name="Estado")
    alianzasolicitante=models.CharField(max_length=100, blank=True, verbose_name="Alianza")
    areasolicitante=models.CharField(max_length=100, blank=True, verbose_name="Area")
    responsable=models.CharField(max_length=100, blank=True, verbose_name="Responsable")
    pasoproduccion=models.CharField(max_length=100, blank=True, verbose_name="Paso Produccion")
    observaciones=models.CharField(max_length=100, blank=True, verbose_name="Observaciones")
    fecharegistro=models.DateTimeField(auto_now_add=True,verbose_name="Fecha Registro BD")
    fecha_actualizacion=models.DateTimeField(auto_now=True,verbose_name="Fecha Actualización BD")
    
    class Meta:
        verbose_name_plural='Requerimientos'
        verbose_name='Requerimiento'
        db_table  = "requerimientos"
        
    def __str__(self):
        return str(self.requerimiento)
    
class HistoricoGeneral(models.Model):
    """Modulo de registros de Logs de cambios"""
    id_historico = models.AutoField(primary_key=True)
    fecha_registro = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Registro")
    usuario = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name="Usuario")
    correo_usuario = models.EmailField(verbose_name="Correo Usuario")
    tipo_cambio = models.CharField(
        max_length=100, verbose_name="Tipo De Cambio")
    tipo_activo = models.CharField(max_length=100, verbose_name="Tipo Activo")
    activo_modificado = models.CharField(
        max_length=100, verbose_name="Activo Modificado")
    valor_anterior = models.CharField(
        max_length=255, default="", verbose_name="Valor Anterior")
    valor_nuevo = models.CharField(
        max_length=255, default="", verbose_name="Valor Nuevo")
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion")

    class Meta:
        verbose_name_plural = 'Historicos'
        verbose_name = 'Historico'
        db_table = 'historico_general'

    def __str__(self):
        return str(self.correo_usuario)