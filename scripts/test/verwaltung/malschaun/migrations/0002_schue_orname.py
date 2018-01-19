# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('malschaun', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schue',
            name='orname',
            field=models.CharField(default=b'a', max_length=1),
        ),
    ]
