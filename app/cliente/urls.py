from django.conf.urls import url, include
from app.cliente.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^registrarse/$',registro_view,name="registrarse"),
	url(r'^perfil/$',login_required(perfil_view),name="perfil"),
   
]
