# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('stock', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('period', models.PositiveSmallIntegerField()),
                ('lastAmtPaid', models.FloatField()),
                ('currentAmtToPay', models.FloatField()),
                ('nextAmtToPay', models.FloatField()),
                ('lastDueDate', models.DateField()),
                ('currentDueDate', models.DateField()),
                ('nextDueDate', models.DateField()),
            ],
        ),
    ]
