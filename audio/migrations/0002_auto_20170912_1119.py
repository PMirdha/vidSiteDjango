# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 11:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextradetail',
            name='mobile_no',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric characters are allowed.')]),
        ),
    ]
