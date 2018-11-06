from django import forms
from .models import Order
import request

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('order', 'customer', 'phone')

    def form_valid(self, form):
        instance = form.save(commit=False)
        print('dfdfdfdfdfdf')
        request.GET('https://api.telegram.org/bot266438341:AAG7xBR40pc-dzZth6TLct-x0S5fhn_MGNQ/sendMessage?chat_id=239840902&text=Новый заказ')
        instance.save()
