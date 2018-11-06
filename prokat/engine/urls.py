from django.urls import path
# from .views import  IndexView,
from . import views


app_name = 'engine'

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'create/', views.CreateOrderView.as_view(), name='order_new'),
    path(r'category/', views.CategoryView.as_view(), name='category_view'),
]
