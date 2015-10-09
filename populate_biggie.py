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

pool_cues = ['JP01-M',
'JP02-M',
'JP03-M',
'JP04-M',
'JP05-M',
'JP06-M',
'JP07-M',
'JP08-M',
'JP09-M',
'JP10-M',
'JP11-M',
'JP12-M',
'JP13-M',
'JP14-M',
'JP15-M',
'JP16-M',
'JP17-M',
'JP18-M',
'JP19-M',
'JP20-M',]


def populate():
    for x in pool_cues:
        make_product('Pechauer JP Series(M)' + ' ' + x)
    print Product.objects.all()

if __name__ == '__main__':
    print "Starting Biggies population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_site.settings')
    populate()

