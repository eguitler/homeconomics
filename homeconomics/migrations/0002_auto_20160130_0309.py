# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeconomics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='currentDueDate',
            new_name='dueDate',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='nextAmtToPay',
            new_name='toPay',
        ),
        migrations.RemoveField(
            model_name='service',
            name='currentAmtToPay',
        ),
        migrations.RemoveField(
            model_name='service',
            name='lastAmtPaid',
        ),
        migrations.RemoveField(
            model_name='service',
            name='lastDueDate',
        ),
        migrations.RemoveField(
            model_name='service',
            name='nextDueDate',
        ),
    ]
