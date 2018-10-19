from app.producto.models import Producto
import simmple_webservice as ws

@ws.register_call(login=True)
def consulta_productos(*kwargs):
	query= Producto.objects.all()
	return ws.query_to_dict(query)