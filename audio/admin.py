# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *#AudioTrackDetail,UserExtraDetail,OrderDetail,AudioTrackGenre

# Register your models here.

admin.site.register(AudioTrackGenre)
admin.site.register(AudioTrackDetail)
admin.site.register(UserExtraDetail)
admin.site.register(OrderDetail)
admin.site.register(OrderItemDetail)
