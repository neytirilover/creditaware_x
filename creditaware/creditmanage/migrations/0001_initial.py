# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='creditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('comp_name', models.CharField(max_length=200)),
                ('ann_fee', models.IntegerField(default=-1)),
                ('reward_type', models.CharField(max_length=20)),
                ('reward_points', models.IntegerField(default=-1)),
                ('reward_dealine', models.FloatField(default=-1.0)),
                ('reward_spend', models.IntegerField(default=-1)),
                ('comment', models.CharField(max_length=500)),
                ('isChase524', models.IntegerField(default=-1)),
                ('isChargeCard', models.IntegerField(default=-1)),
                ('isFirstYearFree', models.IntegerField(default=-1)),
                ('cardGrade', models.IntegerField(default=-1)),
                ('isKeepable', models.IntegerField(default=-1)),
                ('isHotelC', models.IntegerField(default=-1)),
                ('isAirlineC', models.IntegerField(default=-1)),
                ('hasFTF', models.IntegerField(default=-1)),
                ('isDowngradable', models.IntegerField(default=-1)),
                ('id_num', models.IntegerField(default=-1)),
            ],
        ),
    ]
