from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product

# Define the index
@registry.register_document
class ProductDocument(Document):
    name = fields.TextField()
    description = fields.TextField()
    price = fields.FloatField()
    category = fields.KeywordField()
    tags = fields.TextField()

    class Index:
        name = 'products_index'

    class Django:
        model = Product 
