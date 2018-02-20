# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-20 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumeroOrden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_orden', models.SmallIntegerField(verbose_name='Número de Orden')),
                ('vigencia_desde', models.DateField(default=django.utils.timezone.now)),
                ('vigencia_hasta', models.DateField(blank=True, null=True)),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numero_orden_bombero', to='personas.Bombero', verbose_name='Bombero')),
            ],
            options={
                'verbose_name': 'Número de Orden',
                'verbose_name_plural': 'Números de Orden',
            },
        ),
    ]
