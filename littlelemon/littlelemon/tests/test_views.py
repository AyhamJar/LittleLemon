from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu  
from restaurant.serializers import MenuSerializer

class TestMenuView(TestCase):

  def setUp(self):
    self.client = APIClient()
    self.menu1 = Menu.objects.create(Menu_id=1, Title='Veggie Pizza', Price=5.99, Inventory=2)
    self.menu2 = Menu.objects.create(Menu_id=2, Title='Shawerma', Price=9.99, Inventory=3)
    self.menu3 = Menu.objects.create(Menu_id=3, Title='Falafel', Price=14.99, Inventory=5)

  def test_getall(self):
    response = self.client.get(reverse('menu/'))  
    menus = Menu.objects.all()
    serializer = MenuSerializer(menus, many=True)

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, serializer.data)

if __name__ == "__main__":
  TestCase.main()
