# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditmanage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='card_image',
            field=models.ImageField(default=b'card_images/no-img-placeholder.png', upload_to=b'card_images/'),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='card_network',
            field=models.IntegerField(choices=[(0, b'Discover'), (1, b'VISA'), (2, b'MasterCard'), (3, b'American Express'), (4, b'Other')], default=1),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='min_credit_history',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cardGrade',
            field=models.IntegerField(choices=[(0, b'Basic'), (1, b'beginner'), (2, b'Intermediate'), (3, b'Advanced')], default=1),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='hasFTF',
            field=models.IntegerField(choices=[(0, b'False'), (1, b'True')], default=1),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='isAirlineC',
            field=models.IntegerField(choices=[(0, b'False'), (1, b'True')], default=0),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='isChargeCard',
            field=models.IntegerField(choices=[(0, b'False'), (1, b'True')], default=0),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='isChase524',
            field=models.IntegerField(choices=[(0, b'False'), (1, b'True')], default=0),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='isDowngradable',
            field=models.IntegerField(choices=[(0, b'False'), (1, b'True')], default=0),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='isFirstYearFree',
            field=models.IntegerField(choices=[(0, b'False'), (1, b'True')], default=0),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='isHotelC',
            field=models.IntegerField(choices=[(0, b'False'), (1, b'True')], default=0),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='isKeepable',
            field=models.IntegerField(choices=[(0, b'False'), (1, b'True')], default=0),
        ),
    ]