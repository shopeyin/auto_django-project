from django.test import TestCase
from cars.models import Cars
# Create your tests here.


class CarsTestCase(TestCase):
    def setUp(self):
        Cars.objects.create(brand='Toyota')
        Cars.objects.create(brand='Toyota')
    
    def test_check_slugs(self):
        object_1 = Cars.objects.get(pk=1)
        object_2 = Cars.objects.get(pk=2)

        self.assertEqual(object_1.slug,'Toyota')
        self.assertEqual(object_2.slug,'Toyota-2')