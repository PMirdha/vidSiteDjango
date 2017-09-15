from django.conf.urls import url
from . import views

app_name='audio'

urlpatterns = [
	#audio/
    url(r'^$',views.indexView,name='index_view'),
    #audio/registration/
    url(r'^registration/$',views.RegistrationView.as_view(),name='register_view'),
    #audio/login/
    url(r'^login/$',views.LoginView.as_view(),name='login_view'),
    #audio/make_order/
    url(r'^create_order/$',views.CreateOrderView.as_view(),name='create_order_view'),
    #audio/make_order/434/
    #url(r'^create_order/(?P<pk>[0-9]+)/$',views.OrderDetailView.as_view(),name='order_view'),
    url(r'^order_detail/$',views.OrderDetailView.as_view(),name='order_view'),
    #audio/populate_genre/
    url(r'^populate_genre/$',views.GenrePopulateView.as_view(),name='populate_genre_view'),
    #audio/populate_track/
    url(r'^populate_track/$',views.TrackPopulateView.as_view(),name='populate_track_view'),
    
]