# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=50)),
                ('DNI', models.IntegerField()),
                ('Telefono', models.IntegerField()),
                ('Correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=50)),
                ('DNI', models.IntegerField()),
                ('Telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Hora', models.TimeField()),
                ('Doctor', models.ForeignKey(to='AplicacionControlTurnos.Doctor')),
                ('Paciente', models.ForeignKey(to='AplicacionControlTurnos.Paciente')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='Especialidad',
            field=models.ForeignKey(to='AplicacionControlTurnos.Especialidad'),
        ),
    ]
