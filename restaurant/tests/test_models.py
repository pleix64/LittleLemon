from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_menuitem(self):
        menuitem = MenuItem.objects.create(title="Ice Cream", price=6.95, inventory=100)
        self.assertEqual(menuitem.__str__(), "Ice Cream : 6.95")