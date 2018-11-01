from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Category, Good, Order
from django.db.models import Q

def main_list(request):
    return render(request,'engine/index.html')


class ListCategoryView(ListView):
    model = Category
    template_name = 'list_categorys.html'
    context_object_name = 'category'



class ListGoodView(ListView):
    model = Good
    template_name = 'list_goods.html'
    context_object_name = 'good'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('iq')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(category__icontains=query)
            ).distinct()
            self.paginate_by = None
        return queryset

class CreateOrderView(CreateView):
    model = Order
    fields = ('customer', 'phone')
    template_name = 'new_order.html'

    def get_success_url(self):
        return reverse('engine:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('engine:order-create')
        return context
