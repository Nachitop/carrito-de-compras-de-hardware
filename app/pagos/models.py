
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def show_me_the_money(sender, **kwargs):
#     print("hollllllllllllllaaaaaaaa22222222222222222222222")
#     ipn_obj = sender
#     print("entre alv")
#     if ipn_obj.payment_status == ST_PP_COMPLETED:
#         # WARNING !
#         # Check that the receiver email is the same we previously
#         # set on the `business` field. (The user could tamper with
#         # that fields on the payment form before it goes to PayPal)
#         if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
#             # Not a valid payment
#             return

#         # ALSO: for the same reason, you need to check the amount
#         # received, `custom` etc. are all what you expect or what
#         # is allowed.

#         # Undertake some action depending upon `ipn_obj`.
#         #'invoice': 'Test Payment Invoice',
#         if ipn_obj.invoice == "Test Payment Invoice":
#             print("pago recibido")
#         else:
#             printo("Pago no recibido")

#     else:
#         print("nada")
# print("hola1")
# valid_ipn_received.connect(show_me_the_money)
# print("hola3")