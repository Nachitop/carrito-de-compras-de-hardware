"""carrito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views

def login_user(request, template_name='tienda/login.html'):  
    response = auth_views.login(request, template_name)  
    if request.POST.has_key('remember_me'):    
        request.session.set_expiry(1209600)
    return response


urlpatterns = [
    
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^reset/password_reset/$',auth_views.password_reset,{'template_name':'registro/password_reset_form.html','email_template_name':'registro/password_reset_email.html'},name="password_reset"),
    url(r'^password_reset_done/$',auth_views.password_reset_done,{'template_name':'registro/password_reset_done.html'},name="password_reset_done"),
    

    #url(r'^accounts/login/$',auth_views.login,{'template_name': 'tienda/login.html'}, name='login'),
    url(r'^accounts/login/$',login_user, name='login'),
    url(r'^logout/$',auth_views.logout, name='logout'),

    url(r'^admin/', admin.site.urls),
    url(r'^producto/', include('app.producto.urls', namespace="producto")),
    url(r'^cliente/', include('app.cliente.urls', namespace="cliente")),
    url(r'^venta/', include('app.venta.urls', namespace="venta")),
    url(r'^index/', include('app.tienda.urls', namespace="index")),
    url(r'^pagos/', include('app.pagos.urls', namespace="pagos")),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),


    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
