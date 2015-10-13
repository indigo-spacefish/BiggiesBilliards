import os
from oscar.apps.catalogue.models import Product, ProductClass, ProductCategory, Category


product_classes = ProductClass.objects.all()
product_categories = Category.objects.all()
pechauer_cat = product_categories[1]


def make_product(title):
    new_product = Product.objects.get_or_create(
        title=title,
        product_class=product_classes[0],
    )

    new_product[0].save()

    new_cat = ProductCategory.objects.get_or_create(
        product=new_product[0],
        category=pechauer_cat
    )

    new_cat[0].save()

    return new_product


raw_data = '''P04-F
P05-F
P06-F
P07-F
P08-F
P09-F
P10-F
P11-F
P12-F
P13-F
P14-F
P15-F
P16-F
P17-F
P18-F
P19-F
P20-F
P21-F
P22-F
P23-F
P24-F'''

split_data = raw_data.split('\n')

pool_cues = [i for i in split_data]



def populate():
    for x in pool_cues:
        make_product('Pechauer JP Series(M)' + ' ' + x)
    print Product.objects.all()

if __name__ == '__main__':
    print "Starting Biggies population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_site.settings')
    populate()



