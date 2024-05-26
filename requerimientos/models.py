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
    user= models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Usuario")
    
    class Meta:
        verbose_name_plural='Requerimientos'
        verbose_name='Requerimiento'
        db_table  = "requerimientos"
        
    def __str__(self):
        return str(self.requerimiento)