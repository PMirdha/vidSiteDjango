from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from video.models import Playlist,Score

# Create your views here.

def indexView(request):
	"""First page of the site"""
	context={};
	template_name='video/index.html'
	return render(request,template_name,context)

#Only displays objects given to it no relation with model variable
class PlaylistView(generic.ListView):
	model=Score # It does not matter as it only wants object
	template_name='video/playlist.html'
	context_object_name='plist_details'
	def get_queryset(self):
		return Playlist.objects.all()

class ScoreView(generic.DetailView):
	model=Playlist
	template_name='video/score.html'
	context_object_name='plist_details'


