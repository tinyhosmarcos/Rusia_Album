# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cromo',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cromo',
            name='descripcion_text',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='cromo',
            name='tipo',
            field=models.CharField(choices=[('Jugador', 'Jugador'), ('Miscaleneo', 'Miscaleneo')], default='Jugador', max_length=30),
        ),
    ]
