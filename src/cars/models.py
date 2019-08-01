from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from cars.utils import unique_slug_generator
from django.conf import settings
from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver




def upload_location(instance, filename):
	file_path = 'cars/{seller_id}/{brand}-{filename}'.format(
				seller_id=str(instance.seller.id),brand=str(instance.brand), filename=filename)
	return file_path



CONDITION = [
    ('N','New'),
    ('T','Tokunbo'),
    ('NU','Nigerian Use'),
]

FUEL_TYPE = [
    ('P','Petrol'),
    ('D','Diesel'),
    ('E','Electric'),
]





def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    





class Cars(models.Model):
    cars_id                 = models.AutoField(primary_key=True)
    brand					= models.CharField(max_length=50, null=False, blank=False)
    model					= models.CharField(max_length=50, null=False, blank=False)
    year                    = models.IntegerField(('year'), validators=[MinValueValidator(1984), max_value_current_year],null=False, blank=False)
    color					= models.CharField(max_length=50, null=False, blank=False)
    price			    	= models.FloatField(null=False, blank=False)
    condition			    = models.CharField(max_length=2,null=False, blank=False, choices=CONDITION)
    fuel_type			    = models.CharField(max_length=1, verbose_name="fuel type",null=False, blank=False, choices=FUEL_TYPE)
    image		 			= models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_uploaded 			= models.DateTimeField(auto_now_add=True, verbose_name="date uploaded")
    date_updated 			= models.DateTimeField(auto_now=True, verbose_name="date updated")
    seller 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug 					= models.SlugField(blank=True, unique=True)
    def __str__(self):
        return self.brand

@receiver(post_delete,sender=Cars)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_cars_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.brand,instance.slug)
pre_save.connect(pre_save_cars_receiver, sender=Cars)


