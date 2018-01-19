# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('malschaun', '0002_schue_orname'),
    ]

    operations = [
        migrations.CreateModel(
            name='ASchue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('n', models.IntegerField()),
                ('nachname', models.CharField(max_length=1)),
                ('vorname', models.CharField(max_length=1)),
                ('orname', models.CharField(default=b'a', max_length=1)),
                ('jg', models.IntegerField(null=True)),
                ('schuljahr', models.CharField(max_length=5)),
            ],
        ),
    ]
