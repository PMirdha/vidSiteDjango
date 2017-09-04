# -*- coding: utf-8 -*-
#from __future__ import unicode_literalsfrom
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import AudioTrackGenre,OrderDetail

# Create your views here.

def indexView(request):
	context={}
	return render(request,'audio/index.html',context)

class MakeOrderView(generic.ListView):
	template_name='audio/select_order.html'
	context_object_name='audio_track_genre'

	def get_queryset(self):
		return AudioTrackGenre.objects.all()


class OrderDetailView(generic.DetailView):
	template_name='audio/order_detail.html'
	model = OrderDetail