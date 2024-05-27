# Generated by Django 5.0.2 on 2024-05-27 00:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requerimientos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoGeneral',
            fields=[
                ('id_historico', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('correo_usuario', models.EmailField(max_length=254, verbose_name='Correo Usuario')),
                ('tipo_cambio', models.CharField(max_length=100, verbose_name='Tipo De Cambio')),
                ('tipo_activo', models.CharField(max_length=100, verbose_name='Tipo Activo')),
                ('activo_modificado', models.CharField(max_length=100, verbose_name='Activo Modificado')),
                ('valor_anterior', models.CharField(default='', max_length=255, verbose_name='Valor Anterior')),
                ('valor_nuevo', models.CharField(default='', max_length=255, verbose_name='Valor Nuevo')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Historico',
                'verbose_name_plural': 'Historicos',
                'db_table': 'historico_general',
            },
        ),
    ]