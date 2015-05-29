# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='InkindDonation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pc_contact_number', models.CharField(max_length=128)),
                ('sc_contact_number', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1200)),
                ('reason', models.CharField(max_length=1200)),
                ('fair_market_value', models.DecimalField(max_digits=20, decimal_places=2)),
                ('campaign', models.ForeignKey(to='crowdsourcing.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
