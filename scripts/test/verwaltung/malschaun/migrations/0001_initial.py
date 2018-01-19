# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('n', models.IntegerField()),
                ('nachname', models.CharField(max_length=1)),
                ('vorname', models.CharField(max_length=1)),
                ('jg', models.IntegerField(null=True)),
                ('schuljahr', models.CharField(max_length=5)),
            ],
        ),
    ]
