from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse
from .models import Category, Good, Order
from .forms import OrderForm
from django.db.models import Q
from django.shortcuts import redirect
from django import forms

class IndexView(ListView):
    model = Good
    #context_object_name = 'good'
    template_name = 'list_goods.html'
    # queryset = Good.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['good1'] = Good.objects.all()[:3]
        context['good2'] = Good.objects.all()[3:6]
        context['good3'] = Good.objects.all()[6:9]
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


def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('engine:index')
    else:
        form = OrderForm()
        return render(request, 'new_order.html', {'form': form})






# class CreateOrderView(CreateView):
#     model = Order
#     fields = ('order','customer', 'phone')
#     template_name = 'new_order.html'
#
#     def get_success_url(self):
#         return reverse('engine:index')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['action'] = reverse('engine:order-create')
#         return context
