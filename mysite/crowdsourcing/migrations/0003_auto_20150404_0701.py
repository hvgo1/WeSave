# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0002_auto_20150403_1639'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.AlterField(
            model_name='individual',
            name='birthday',
            field=models.DateField(verbose_name=b'birthday'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'profile_images/', blank=True),
            preserve_default=True,
        ),
    ]
