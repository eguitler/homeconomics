# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeconomics', '0002_auto_20160130_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period', models.PositiveSmallIntegerField()),
                ('amount', models.FloatField()),
                ('dueDate', models.DateField()),
                ('parent', models.ForeignKey(to='homeconomics.History')),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='dueDate',
        ),
        migrations.RemoveField(
            model_name='service',
            name='period',
        ),
        migrations.RemoveField(
            model_name='service',
            name='toPay',
        ),
    ]
