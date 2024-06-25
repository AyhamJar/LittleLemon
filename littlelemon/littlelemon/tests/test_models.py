from django.test import TestCase
from restaurant.models import Menu

class TestMenu(TestCase):
  def test_menu_str(self):
    item = Menu.objects.create(Menu_id=1, Title='Steak', Price=6.99, Inventory=10)
    self.assertEqual(str(item), 'Steak : 6.99')