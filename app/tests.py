from django.test import TestCase
from .models import Item

class ItemModelTest(TestCase):
    def setUp(self):
        Item.objects.create(name='Test Item', description='Test Description')

    def test_item_name(self):
        item = Item.objects.get(name='Test Item')
        self.assertEqual(item.name, 'Test Item')

    def test_item_description(self):
        item = Item.objects.get(name='Test Item')
        self.assertEqual(item.description, 'Test Description')
