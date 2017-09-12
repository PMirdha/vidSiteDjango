from django.conf.urls import url
from . import views

app_name='audio'

urlpatterns = [
	#audio/
    url(r'^$',views.indexView,name='index_view'),
    #audio/make_order/
    url(r'^create_order/$',views.CreateOrderView.as_view(),name='create_order_view'),
    #audio/make_order/434/
    url(r'^create_order/(?P<pk>[0-9]+)/$',views.OrderDetailView.as_view(),name='order_view'),
    #audio/registration/
    url(r'^registration/$',views.RegistrationView.as_view(),name='register_view'),
    
]