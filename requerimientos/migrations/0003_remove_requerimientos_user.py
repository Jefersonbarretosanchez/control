# Generated by Django 5.0.2 on 2024-05-27 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requerimientos', '0002_historicogeneral'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requerimientos',
            name='user',
        ),
    ]
