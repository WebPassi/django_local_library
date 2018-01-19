# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Textaufgabe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('bereich', models.CharField(max_length=10)),
                ('inhalt', models.CharField(max_length=10)),
                ('schwierigkeit', models.IntegerField()),
                ('punkte', models.IntegerField()),
            ],
        ),
    ]
