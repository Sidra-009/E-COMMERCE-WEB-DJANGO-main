import csv
from django.core.management.base import BaseCommand
from myapp.models import Product, SubCategory  # adjust your import

class Command(BaseCommand):
    help = 'Import products from CSV'

    def handle(self, *args, **kwargs):
        with open(r'D:\cartify\E-COMMERCE-WEB-DJANGO-main\fashion_products.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                subcat = SubCategory.objects.get(id=row['sub_category_id'])
                Product.objects.create(
                    name=row['name'],
                    slug=row['slug'],
                    price=row['price'],
                    old_price=row['old_price'],
                    description=row['description'],
                    stock=row['stock'],
                    image=row['image'],
                    created_at=row['created_at'],
                    updated_at=row['updated_at'],
                    sub_category=subcat
                )
        self.stdout.write(self.style.SUCCESS('Products imported successfully!'))
