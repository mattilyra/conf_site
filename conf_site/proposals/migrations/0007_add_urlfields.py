# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-06 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0006_add_date_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='code_url',
            field=models.URLField(default=b'', help_text=b"Location of this proposal's code repository.", max_length=2083, verbose_name=b'Repository'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='slides_url',
            field=models.URLField(default=b'', help_text=b'Location of slides for this proposal.', max_length=2083, verbose_name=b'Slides'),
        ),
    ]
