# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 08:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0002_auto_20170831_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextradetail',
            name='mobile_no',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)]),
        ),
    ]
