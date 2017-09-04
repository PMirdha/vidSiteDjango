from django.conf.urls import url
from . import views

urlpatterns = [
	#audio/
    url(r'^$',views.indexView,name='index_view'),
    #audio/make_order/
    url(r'^create_order/$',views.MakeOrderView.as_view(),name='make_order_view'),
    #audio/make_order/434/
    url(r'^create_order/(?P<pk>[0-9]+)/$',views.OrderDetailView.as_view(),name='order_view'),
    #video/playlist
    #url(r'^playlist/$',views.PlaylistView.as_view(),name='playlist-view'),
    #video/playlist/111/
    #url(r'^playlist/(?P<pk>[0-9]+)/$',views.ScoreView.as_view(),name='score-view'),
]