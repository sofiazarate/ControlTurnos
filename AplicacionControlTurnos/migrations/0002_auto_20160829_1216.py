# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AplicacionControlTurnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorariosLaborales',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Dia', models.IntegerField(default=0, choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'), (0, 'Domingo')])),
                ('HoraInicio', models.TimeField()),
                ('HoraFin', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='HorariosLaborales',
            field=models.ForeignKey(to='AplicacionControlTurnos.HorariosLaborales', default=0),
            preserve_default=False,
        ),
    ]
