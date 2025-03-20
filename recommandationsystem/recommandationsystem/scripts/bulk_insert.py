import os
import django
import random
from decimal import Decimal
from django.utils.text import slugify

# Setup Django Environment


from ..search.models import Product 

# Sample Data for Categories and Tags
CATEGORIES = ['Electronics', 'Clothing', 'Books', 'Home Appliances', 'Toys', 'Automobiles']
TAGS = ['sale', 'new', 'popular', 'discount', 'best-seller']

# Function to Generate and Insert Bulk Products
def generate_products(batch_size=10000, total_records=10000000):
    products = []
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

        # Insert in Batches
        if len(products) >= batch_size:
            Product.objects.bulk_create(products)
            print(f'Inserted {len(products)} records...')
            products.clear()

    # Insert remaining products
    if products:
        Product.objects.bulk_create(products)
        print(f'Inserted last batch of {len(products)} records...')

# Run the function inside a Django environment
if __name__ == '__main__':
    print('buld inserted')
    generate_products()
