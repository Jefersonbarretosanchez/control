# Generated by Django 5.0.2 on 2024-05-26 23:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Requerimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=100, verbose_name='# Ticket')),
                ('requerimiento', models.CharField(blank=True, max_length=100, verbose_name='Nombre Requerimientos')),
                ('fechacreacion', models.DateField(verbose_name='Fecha Creación')),
                ('mediocarga', models.CharField(blank=True, max_length=100, verbose_name='Medio Carga')),
                ('plataforma', models.CharField(blank=True, max_length=100, verbose_name='Plataforma')),
                ('estado', models.CharField(blank=True, max_length=100, verbose_name='Estado')),
                ('alianzasolicitante', models.CharField(blank=True, max_length=100, verbose_name='Alianza')),
                ('areasolicitante', models.CharField(blank=True, max_length=100, verbose_name='Area')),
                ('responsable', models.CharField(blank=True, max_length=100, verbose_name='Responsable')),
                ('pasoproduccion', models.CharField(blank=True, max_length=100, verbose_name='Paso Produccion')),
                ('observaciones', models.CharField(blank=True, max_length=100, verbose_name='Observaciones')),
                ('fecharegistro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Registro BD')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización BD')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Requerimiento',
                'verbose_name_plural': 'Requerimientos',
                'db_table': 'requerimientos',
            },
        ),
    ]
