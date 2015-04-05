# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings

import django_countries.fields



class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),

                ('country', django_countries.fields.CountryField(max_length=2)),

                ('street', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Barangay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('beneficiary_name', models.CharField(max_length=200)),
                ('story', models.CharField(max_length=2000)),
                ('deadline', models.DateTimeField(verbose_name=b'deadline')),
                ('status', models.CharField(default=b'D', max_length=15, choices=[(b'D', b'Draft'), (b'F', b'For Approval'), (b'V', b'Verified'), (b'C', b'Completed'), (b'I', b'Inactive')])),
                ('views', models.BigIntegerField(default=0)),

                ('ack_receipt', models.ImageField(null=True, upload_to=b'ack_receipts/', blank=True)),
                ('campaign_image', models.ImageField(null=True, upload_to=b'profile_images/', blank=True)),

                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campaign_Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campaign', models.ForeignKey(to='crowdsourcing.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campaign_User_Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=20, decimal_places=2)),
                ('campaign', models.ForeignKey(to='crowdsourcing.Campaign')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campaign_Wish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('completed', models.BooleanField()),
                ('estimated_price', models.DecimalField(max_digits=20, decimal_places=2)),
                ('campaign', models.ForeignKey(to='crowdsourcing.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('message', models.CharField(max_length=200)),
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
                ('page_address', models.URLField(null=True, blank=True)),
                ('about', models.CharField(max_length=200)),
                ('registration_number', models.BigIntegerField(null=True, blank=True)),

                ('document', models.FileField(null=True, upload_to=b'documents/', blank=True)),

                ('comments', models.CharField(max_length=200, null=True, blank=True)),
                ('pc_first_name', models.CharField(max_length=200)),
                ('pc_last_name', models.CharField(max_length=200)),
                ('pc_email', models.EmailField(max_length=75)),
                ('pc_job_title', models.CharField(max_length=200)),
                ('pc_phone_number', models.CharField(max_length=12)),
                ('sc_first_name', models.CharField(max_length=200)),
                ('sc_last_name', models.CharField(max_length=200)),
                ('sc_email', models.EmailField(max_length=75)),
                ('sc_job_title', models.CharField(max_length=200)),
                ('sc_phone_number', models.CharField(max_length=12)),
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
                ('middle_name', models.CharField(max_length=200, null=True, blank=True)),
                ('last_name', models.CharField(max_length=200)),

                ('birthday', models.DateField(verbose_name=b'birthday')),

                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unregistered_Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.DecimalField(max_digits=20, decimal_places=2)),
                ('campaign', models.ForeignKey(to='crowdsourcing.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),

                ('photo', models.ImageField(null=True, upload_to=b'profile_images/', blank=True)),
                ('role', models.CharField(max_length=15, choices=[(b'Ben', b'Beneficiary'), (b'Hos', b'Hospital Representative'), (b'Don', b'Donor'), (b'Adm', b'Admin')])),

                ('address', models.ForeignKey(to='crowdsourcing.Address')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('wish_type', models.CharField(max_length=10, choices=[(b'0', b'Cash'), (b'1', b'In-Kind')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='service_category',

            field=models.ManyToManyField(to='crowdsourcing.Service_Category'),

            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign_wish',
            name='wish',
            field=models.ForeignKey(to='crowdsourcing.Wish'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign_keyword',
            name='keyword',
            field=models.ForeignKey(to='crowdsourcing.Keyword'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='donors',
            field=models.ManyToManyField(related_name='campaign_donors', through='crowdsourcing.Campaign_User_Donor', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='keywords',
            field=models.ManyToManyField(to='crowdsourcing.Keyword', through='crowdsourcing.Campaign_Keyword'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='subscribers',
            field=models.ManyToManyField(related_name='campaign_subscribers', through='crowdsourcing.Campaign_User_Followers', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='wishes',
            field=models.ManyToManyField(to='crowdsourcing.Wish', through='crowdsourcing.Campaign_Wish'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='barangay',
            field=models.ForeignKey(blank=True, to='crowdsourcing.Barangay', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, to='crowdsourcing.City', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',

            name='region',
            field=models.ForeignKey(blank=True, to='crowdsourcing.Region', null=True),
            preserve_default=True,
        ),
    ]
