# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('beneficiary_name', models.CharField(max_length=200)),
                ('story', models.CharField(max_length=2000)),
                ('deadline', models.DateTimeField(verbose_name=b'deadline')),
                ('approval_tag', models.BooleanField()),
                ('status', models.IntegerField()),
                ('views', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campaign_User_Followers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campaign', models.ForeignKey(to='crowdsourcing.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campaign_Wishlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receive_tag', models.BooleanField()),
                ('campaign', models.ForeignKey(to='crowdsourcing.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birthday', models.DateTimeField(verbose_name=b'birthday')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('barangay', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=100)),
                ('photo', models.ImageField(null=True, upload_to=None, blank=True)),
                ('location', models.ForeignKey(to='crowdsourcing.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.ForeignKey(to='crowdsourcing.Role')),
                ('user', models.ForeignKey(to='crowdsourcing.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WishType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='wish_type',
            field=models.ForeignKey(to='crowdsourcing.WishType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='individual',
            name='user',
            field=models.ForeignKey(to='crowdsourcing.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(to='crowdsourcing.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign_wishlist',
            name='wishlist',
            field=models.ForeignKey(to='crowdsourcing.Wishlist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign_user_followers',
            name='user',
            field=models.ForeignKey(to='crowdsourcing.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='created_by',
            field=models.ForeignKey(to='crowdsourcing.User'),
            preserve_default=True,
        ),
    ]
