from django.views.generic import ListView, CreateView
from django.urls import reverse
from .models import Category, Good, Order
from django.db.models import Q



class IndexView(ListView):
    template_name = 'list_goods.html'
    queryset = Good.objects.all()

    def get_context_data(self, **kwargs):
        n = 3
        context = super(IndexView, self).get_context_data(**kwargs)
        queryset = super().get_queryset()

        context['request'] = self.request
        context['category'] = Category.objects.all()
        query = self.request.GET.get('iq')
        if query:
            tempquery = Good.objects.all().filter(Q(name__icontains=query) | Q(category__name__icontains=query))
            if len(tempquery) == 4:  # Блок извращений для корректного отображения товаров в сетке бутстрапа
                context['goodcheck'] = 'Oh no 4'  # Создание переменной которая укажет в шаблоне list_goods что у нас 4 товара
                n = 2
            else:  # Формируем 3 корректных столбца, для отображения в сетке бутстрапа
                n = round((len(tempquery) / 3) + 0.2)  # Чтоб не импортировать math ради одной строки
            context['good1'] = tempquery[:n]
            context['good2'] = tempquery[n:n * 2]
            context['good3'] = tempquery[n * 2:n * 3]
        else:
            context['good1'] = queryset.all()[:n]
            context['good2'] = queryset.all()[n:n * 2]
            context['good3'] = queryset.all()[n * 2:n * 3]
        return context


class CategoryView(ListView):
    template_name = 'list_categorys.html'
    context_object_name = 'goods'
    queryset = Good.objects.filter(id=1)


class CreateOrderView(CreateView):
    model = Order
    fields = ('order', 'customer', 'phone')
    template_name = 'new_order.html'

    def get_success_url(self):
        # print(Order.pk)
        return reverse('engine:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('engine:order_new')
        return context

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     print('dfdfdfdfdfdf')
    #     # request.GET('https://api.telegram.org/bot266438341:AAG7xBR40pc-dzZth6TLct-x0S5fhn_MGNQ/sendMessage?chat_id=239840902&text=Новый заказ')
    #     instance.save()
