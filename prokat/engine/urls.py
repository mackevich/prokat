from django.urls import path
from .views import ListGoodView, ListCategoryView, IndexView

app_name = 'engine'

urlpatterns = [
   # path('', main_list),
    path(r'', IndexView.as_view(), name='index'),
]
