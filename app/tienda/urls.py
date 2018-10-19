# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib.auth.views import login, password_reset, password_reset_confirm,password_reset_complete, password_reset_done
from app.tienda.views import Index, recien_llegado,obtener_ofertas_inicio, ofertas_listado, obtener_productos_nuevos_inicio, obtener_productos_nuevos, obtener_marcas,obtener_marcas_productos, obtener_ofertas, obtener_marcas_ofertas,obtener_productos_marcas_ofertas,categorias, ir_categoria, obtener_producto, obtener_comentarios, hacer_comentario,editar_comentario, obtener_determinados_productos,obtener_productos_por_categoria
from app.tienda.views import favoritos
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from app.tienda.views import obtener_total_carrito,obtener_cantidad_favorito, carrito, ver_carrito,obtener_listado_favoritos,eliminar_de_favoritos,historial_compras,factura_compra_pdf,obtenerDescripcionProducto, verificar_producto
urlpatterns = [
    
url(r'^$', Index.as_view(), name="index"),
url(r'^recien_llegado/', recien_llegado, name="recien_llegado"),
url(r'^ofertas/', ofertas_listado, name="ofertas_listado"),
#url(r'^ajax/obtener_marcas/$', obtener_marcas, name="obtener_marcas"),
url(r'^categorias/$', categorias,name="categorias"),
url(r'^carrito/$', carrito,name="carrito"),
url(r'^categorias/(?P<categoria>\d+)/$', ir_categoria, name="ir_categoria"),
url(r'^producto=(?P<id_pro>\d+)/$', obtener_producto, name="obtener_producto"),
url(r'^ajax/obtener_comentarios/$',obtener_comentarios, name="obtener_comentarios"),
url(r'^ajax/hacer_comentario/$',hacer_comentario, name="hacer_comentario"),
url(r'^ajax/editar_comentario/$',editar_comentario, name="editar_comentario"),
url(r'^ajax/obtener_ofertas_inicio/$',obtener_ofertas_inicio, name="obtener_ofertas_inicio"),
url(r'^ajax/obtener_productos_nuevos_inicio/$', obtener_productos_nuevos_inicio, name="obtener_productos_nuevos_inicio"),
url(r'^ajax/obtener_productos_nuevos/$', obtener_productos_nuevos, name="obtener_productos_nuevos"),
url(r'^ajax/obtener_marcas/$', obtener_marcas, name="obtener_marcas"),
url(r'^ajax/obtener_marcas_ofertas/$', obtener_marcas_ofertas, name="obtener_marcas_ofertas"),
url(r'^ajax/obtener_ofertas/$', obtener_ofertas, name="obtener_ofertas"),
url(r'^ajax/obtener_marcas_productos/$', obtener_marcas_productos, name="obtener_marcas_productos"),
url(r'^ajax/obtener_productos_marcas_ofertas/$', obtener_productos_marcas_ofertas, name="obtener_productos_marcas_ofertas"),

url(r'^ajax/obtener_determinados_productos/$', obtener_determinados_productos, name="obtener_determinados_productos"),
url(r'^ajax/obtener_productos_por_categoria/$', obtener_productos_por_categoria, name="obtener_productos_por_categoria"),

url(r'^ajax/obtener_total_carrito/$', obtener_total_carrito, name="obtener_total_carrito"),
url(r'^ajax/obtener_cantidad_favorito/$', obtener_cantidad_favorito, name="obtener_cantidad_favorito"),
url(r'^ajax/ver_carrito/$', ver_carrito, name="ver_carrito"),
url(r'^ajax/obtener_listado_favoritos/$', obtener_listado_favoritos, name="obtener_listado_favoritos"),
url(r'^ajax/eliminar_de_favoritos/$', eliminar_de_favoritos, name="eliminar_de_favoritos"),
url(r'^ajax/obtenerDescripcionProducto/$', obtenerDescripcionProducto, name="obtenerDescripcionProducto"),
url(r'^ajax/verificar_producto/$', verificar_producto, name="verificar_producto"),
#url(r'',password_reset,{'template_name': 'registro/password_reset_form.html','email_template_name':'registro/password_reset_email.html'},name='password_reset'),
url(r'^reset/(?P<uidb64>[0-94-Za-z_\-]+)/(?P<token>.+)/$',auth_views.password_reset_confirm,{'template_name':'registro/password_reset_confirm.html'},name="password_reset_confirm"),
url(r'^reset/complete/$',password_reset_complete,{'template_name':'registro/password_reset_complete.html'},name="password_reset_complete"),

url(r'^favoritos/$',login_required(favoritos),name="favoritos"),
url(r'^historial_compras/$',login_required(historial_compras),name="historial_compras"),

url(r'^factura_compra_pdf=(?P<slug>[a-zA-Z0-9-]+)/$',login_required(factura_compra_pdf.as_view()), name="factura_compra_pdf"),
]
