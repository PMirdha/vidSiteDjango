# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 04:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_auto_20170831_0842'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AudioTrackDetail',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='userextradetail',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
        migrations.DeleteModel(
            name='UserExtraDetail',
        ),
    ]