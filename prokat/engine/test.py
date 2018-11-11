from django.test import TestCase
import datetime
from .models import Category, Good, Order


class ObjectCreateTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Tools', description='Building tools')
        Category.objects.create(name='Protection means', description='Means of protection', ranking=15)
        tools = Category.objects.get(name='Tools')
        protection = Category.objects.get(name='Protection means')
        Good.objects.create(category=tools, name='Perforator', description='Drilling holes',
                            price=15)
        Good.objects.create(category=protection, name='Gloves', description='Hand protection',
                            price=3, ranking=88)
        perforator = Good.objects.get(name='Perforator')
        gloves = Good.objects.get(name='Gloves')
        Order.objects.create(customer='Vasya Pupkin', phone='375296666666', order=perforator )
        Order.objects.create(customer='Al Lukashenko', phone='375297777777', order=gloves )


    def test_category_object(self):
        """Test Category object run - correctly create object Category model"""
        print('Test Category object run - correctly create object Category model')
        tools = Category.objects.get(name="Tools")
        protection = Category.objects.get(name="Protection means")
        self.assertEqual(tools.id, 1)
        self.assertEqual(tools.description, 'Building tools')
        self.assertEqual(type(tools.created), datetime.datetime)
        self.assertEqual(tools.ranking, 0)
        self.assertEqual(protection.id, 2)
        self.assertEqual(protection.description, 'Means of protection')
        self.assertEqual(type(protection.created), datetime.datetime)
        self.assertEqual(protection.ranking, 15)


    def test_good_object(self):
        """Test Good object run - correctly create object Good model"""
        print('Test Good object run - correctly create object Good model')
        perforator = Good.objects.get(name='Perforator')
        gloves = Good.objects.get(name='Gloves')
        self.assertEqual(perforator.id, 1)
        self.assertEqual(perforator.description, 'Drilling holes')
        self.assertEqual(type(perforator.created), datetime.datetime)
        self.assertEqual(perforator.ranking, 0)
        self.assertEqual(perforator.price, 15)
        self.assertEqual(gloves.id, 2)
        self.assertEqual(gloves.description, 'Hand protection')
        self.assertEqual(type(gloves.created), datetime.datetime)
        self.assertEqual(gloves.price, 3)
        self.assertEqual(gloves.ranking, 88)


    def test_order_object(self):
        """Test Order object run - correctly create object Order model"""
        print('Test Order object run - correctly create object Order model')
        vasya = Order.objects.get(customer='Vasya Pupkin')
        lunalikiy = Order.objects.get(customer='Al Lukashenko')
        self.assertEqual(vasya.id, 1)
        self.assertEqual(vasya.phone, '375296666666')
        self.assertEqual(type(vasya.created), datetime.datetime)
        self.assertEqual(lunalikiy.id, 2)
        self.assertEqual(lunalikiy.phone, '375297777777')
        self.assertEqual(type(lunalikiy.created), datetime.datetime)






