from django.urls import path
from .views import ListGoodView, ListCategoryView

app_name = 'engine'

urlpatterns = [
   # path('', main_list),
    path(r'', ListGoodView.as_view(), name='index'),
]
