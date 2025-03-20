import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from search.models import Product  # Import the Product model
from django.db import transaction

# Sample Categories & Tags
CATEGORIES = ['Electronics', 'Clothing', 'Books', 'Home Appliances', 'Toys', 'Automobiles']
TAGS = ['sale', 'new', 'popular', 'discount', 'best-seller']

class Command(BaseCommand):
    help = "Populates the Product table with (1 million) records"

    def handle(self, *args, **kwargs):
        total_records = 1000000  # 10 lakh records
        batch_size = 10000  # Insert 10,000 at a time
        products = []

        self.stdout.write(self.style.SUCCESS("Starting bulk insert..."))

        for i in range(total_records):
            name = f'Product {i}'
            description = f'Description for product {i}'
            price = Decimal(random.uniform(10, 10000)).quantize(Decimal('0.01'))
            category = random.choice(CATEGORIES)
            tags = ', '.join(random.sample(TAGS, random.randint(1, 3)))

            product = Product(
                name=name,
                description=description,
                price=price,
                category=category,
                tags=tags
            )
            products.append(product)

            # Insert in batches
            if len(products) >= batch_size:
                Product.objects.bulk_create(products)
                self.stdout.write(self.style.SUCCESS(f'Inserted {len(products)} records...'))
                products.clear()

        # Insert remaining records
        if products:
            Product.objects.bulk_create(products)
            self.stdout.write(self.style.SUCCESS(f'Inserted last batch of {len(products)} records...'))

        self.stdout.write(self.style.SUCCESS("Bulk insert completed successfully!"))
