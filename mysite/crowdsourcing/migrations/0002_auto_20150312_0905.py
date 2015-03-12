# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign_wishlist',
            old_name='receive_tag',
            new_name='received_tag',
        ),
    ]
