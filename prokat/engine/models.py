from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True,
                            on_delete=models.CASCADE, )
    image = models.ImageField(default='no_image.jpeg')
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now=True)
    ranking = models.DecimalField(max_digits=100, decimal_places=0, default=0, )

    def __str__(self):
        return self.name

    class Meta:  # Допилить не работает
        ordering = ['ranking']


class Good(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )
    image = models.ImageField(default='no_image.jpeg')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    price = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now=True)
    ranking = models.DecimalField(max_digits=100, decimal_places=0, default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-ranking']


class Order(models.Model):
    customer = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=18, verbose_name='Телефон')
    order = models.ForeignKey(Good, verbose_name='Товар', on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone
