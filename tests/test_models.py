from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuTest(TestCase):
    def test_menu_str(self):
        menu_item = Menu.objects.create(title="Pasta", price=12.99)
        self.assertEqual(str(menu_item), "Pasta : 12.99")

class MenuViewTest(APITestCase):
    def setUp(self):
        self.menu_item1 = Menu.objects.create(title="Pasta", price=12.99)
        self.menu_item2 = Menu.objects.create(title="Pizza", price=9.99)
        self.menu_item3 = Menu.objects.create(title="Salad", price=7.99)

    def test_getall(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)