from django.conf.urls import url
from . import views


app_name='video'

urlpatterns = [
	#video/
    url(r'^$',views.indexView,name='index-view'),
    #video/playlist
    url(r'^playlist/$',views.PlaylistView.as_view(),name='playlist-view'),
    #video/playlist/111/
    url(r'^playlist/(?P<pk>[0-9]+)/$',views.ScoreView.as_view(),name='score-view'),
]