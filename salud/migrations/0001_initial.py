# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-06 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alergenos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_alergeno', models.CharField(max_length=255, verbose_name='Nombre del Alérgeno')),
            ],
            options={
                'verbose_name': 'Alérgeno',
                'verbose_name_plural': 'Alérgenos',
            },
        ),
        migrations.CreateModel(
            name='Alergicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observaciones')),
                ('alergeno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salud.Alergenos', verbose_name='Alérgeno')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Bombero', verbose_name='Bombero')),
            ],
            options={
                'verbose_name': 'Alérgico',
                'verbose_name_plural': 'Alérgicos',
            },
        ),
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personas.Institucion', verbose_name='Institución')),
            ],
            options={
                'verbose_name': 'Clínica',
                'verbose_name_plural': 'Clínicas',
            },
        ),
        migrations.CreateModel(
            name='CoberturaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroAfiliado', models.CharField(max_length=11, unique=True, verbose_name='Número de Afiliado')),
                ('fechaInicio', models.DateField(null=True, verbose_name='Fecha de Inicio de Cobertura')),
                ('fechaFin', models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización de Cobertura')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observaciones')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Bombero', verbose_name='Bombero')),
                ('clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salud.Clinica', verbose_name='Clínica')),
            ],
            options={
                'verbose_name': 'Cobertura Médica',
                'verbose_name_plural': 'Coberturas Médicas',
            },
        ),
        migrations.CreateModel(
            name='MedicoCabecera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=255, verbose_name='Apellido')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('especialidad', models.CharField(max_length=255, verbose_name='Especialidad')),
                ('nroMatricula', models.CharField(max_length=11, unique=True, verbose_name='Número de Matrícula')),
            ],
            options={
                'verbose_name': 'Médico de Cabecera',
                'verbose_name_plural': 'Médicos de Cabecera',
            },
        ),
        migrations.CreateModel(
            name='ObraSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personas.Institucion', verbose_name='Institución')),
            ],
            options={
                'verbose_name': 'Obra Social',
                'verbose_name_plural': 'Obras Sociales',
            },
        ),
        migrations.CreateModel(
            name='PlanMedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=255, verbose_name='Descripción')),
                ('obraSocial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obraSocial', to='salud.ObraSocial', verbose_name='Obra Social')),
            ],
            options={
                'verbose_name': 'Plan Médico',
                'verbose_name_plural': 'Planes Médicos',
            },
        ),
        migrations.AlterUniqueTogether(
            name='medicocabecera',
            unique_together=set([('nombre', 'apellido', 'nroMatricula')]),
        ),
        migrations.AddField(
            model_name='coberturamedica',
            name='medicoCabecera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salud.MedicoCabecera', verbose_name='Médico de Cabecera'),
        ),
        migrations.AddField(
            model_name='coberturamedica',
            name='planMedico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salud.PlanMedico', verbose_name='Plan Médico'),
        ),
        migrations.AlterUniqueTogether(
            name='coberturamedica',
            unique_together=set([('bombero', 'planMedico')]),
        ),
        migrations.AlterUniqueTogether(
            name='alergicos',
            unique_together=set([('bombero', 'alergeno')]),
        ),
    ]
