import os

from django.db import models
from ckeditor.fields import RichTextField
import random
from django.conf import settings
from font_icons.models import IconForeignKeyField
# from django.contrib.gis.utils import GeoIP
import requests
import googlemaps


# Create your models here.

def image_path(instance, filename):
    base_name, f_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''.join((random.choice(chars)) for _ in range(20))
    return 'aboutus/about_img_{randomstring}{ext}'.format(basename=base_name, randomstring=random_str, ext=f_extension)


class about_us(models.Model):
    title = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        return "%s/%s" % (settings.MEDIA_URL, self.image)


class sociallinks(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=600)
    icon = IconForeignKeyField(on_delete=True, null=True, blank=True)

    def __str__(self):
        return self.name


class company_address(models.Model):
    title = models.CharField(max_length=100)
    title_desc = models.CharField(max_length=255)
    address_title = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=400)

    def __str__(self):
        return self.title

class dynAddress(models.Model):
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')

    def __str__(self):
        return f'Adresse de {self.address_1}'

    class Meta:
        verbose_name_plural = "addresses"

    def save(self, **kwargs):
        df = None
        address = " ".join([self.address_1, self.address_2, str(self.zip_code), self.city])
        print('address:',address)
        api_key = "AIzaSyBERbMA-_M3emhp9ZFzrJVYuBy__Va3kr4"
        # google_map_key = googlemaps.Client(key="AIzaSyBERbMA-_M3emhp9ZFzrJVYuBy__Va3kr4")
        api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()
        print('response status: ',api_response_dict['status'])
        if api_response_dict['status'] == 'OK':
            self.latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            self.longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            self.save()
        super().save(**kwargs)


class copyright(models.Model):
    copyright = models.CharField(max_length=255)

    def __str__(self):
        return self.copyright
