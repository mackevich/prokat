from django.urls import path
from .views import main_list, ListCategoryView

app_name = 'engine'

urlpatterns = [
   # path('', main_list),
    path(r'', ListCategoryView.as_view(), name='index'),
]
