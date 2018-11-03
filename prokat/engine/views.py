from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse
from .models import Category, Good, Order
from django.db.models import Q

class IndexView(ListView):
    #model = Good
    #context_object_name = 'good'
    template_name = 'list_goods.html'
    queryset = Good.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['good'] = Good.objects.all()
        # And so on for more models
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('iq')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query)
            ).distinct()
            self.paginate_by = None
        return queryset



class CreateOrderView(CreateView):
    model = Order
    fields = ('order','customer', 'phone')
    template_name = 'new_order.html'

    def get_success_url(self):
        return reverse('engine:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('engine:order-create')
        return context
