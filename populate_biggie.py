import os
from django.db import models
# from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractProductClass, AbstractProductCategory
from oscar.apps.catalogue.models import Product, ProductClass, ProductCategory

def make_product(title):
    new_product = Product.objects.get_or_create(
        title=title,
        product_class=models.ForeignKey(ProductClass),
        categories=models.ManyToManyField(ProductCategory, through='ProductCategory'),
    )
    new_product.save()

pool_cues = ['meow', 'Leia', 'tasty']

def populate():
    for x in pool_cues:
        make_product(x)
    print Product.objects.all()

if __name__ == '__main__':
    print "Starting Biggies population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_site.settings')
    populate()
