from django.contrib import admin
from .models import Category, Good, Order


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image','description','ranking','created')
    search_fields = ('name', 'description')


    class Meta:
        model = Category

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('category','name','description','price','ranking','created')


    class Meta:
        model = Good

@admin.register(Order)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('order','customer','phone','created')

    class Meta:
        model = Order
