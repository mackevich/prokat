from django.urls import path
from .views import  IndexView, CreateOrderView

app_name = 'engine'

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),
    path(r'create/', CreateOrderView.as_view(), name='order-create'),
]
