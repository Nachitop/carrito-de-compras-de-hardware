from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [

	url(r'^process/$',login_required(views.payment_process),name='process'),
	url(r'^done/$',login_required(views.payment_done),name='done'),
	url(r'^canceled/$',login_required(views.payment_canceled),name='canceled'),

	url(r'^ajax/recibir_carrito/$',views.recibir_carrito,name='recibir_carrito'),


]