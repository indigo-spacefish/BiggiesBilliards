import os
from oscar.apps.catalogue.models import Product, ProductClass, ProductCategory, Category
from oscar.apps.partner.models import StockRecord, Partner


product_classes = ProductClass.objects.all()
product_categories = Category.objects.all()
pechauer_cat = product_categories[1]
partners = Partner.objects.all()
biggies_partner = partners[2]


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

    new_record = StockRecord.objects.get_or_create(
        partner=biggies_partner,
        product=new_product[0],
        partner_sku=title,
    )

    new_record[0].save()

    return new_product


raw_data = '''JP03-M
JP04-M
JP05-M
JP06-M
JP07-M
JP08-M
JP09-M
JP10-M
JP11-M
JP12-M
JP13-M
JP14-M
JP15-M
JP16-M
JP17-M
JP18-M
JP19-M
JP20-M'''

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
