# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inkinddonation',
            old_name='reason',
            new_name='remarks',
        ),
    ]
