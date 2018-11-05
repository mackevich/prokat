from django.urls import path
# from .views import  IndexView,
from . import views

app_name = 'engine'

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    # path(r'create/$', CreateOrderView.as_view(), name='order-create'),
    path(r'create/', views.order_new, name='order_new'),
]
