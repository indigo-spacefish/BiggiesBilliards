import os
from oscar.apps.catalogue.models import Product, ProductClass, ProductCategory

product_classes = ProductClass.objects.all()
product_categories = ProductCategory.objects.all()

def make_product(title):
    new_product = Product.objects.get_or_create(
        title=title,
        product_class=product_classes[0],
#        categories=ProductCategory,
    )
    new_product[0].save()
    return new_product

pool_cues = ['cue_1', 'cue_2', 'cue_3']

def populate():
    for x in pool_cues:
        make_product(x)
    print Product.objects.all()

if __name__ == '__main__':
    print "Starting Biggies population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_site.settings')
    populate()
