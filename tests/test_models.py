import unittest
from service.models import Product, db
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    def setUp(self):
        db.drop_all()
        db.create_all()

    def test_create_product(self):
        product = ProductFactory()
        product.create()
        self.assertIsNotNone(product.id)

    def test_update_product(self):
        product = ProductFactory()
        product.create()
        product.name = "Updated"
        product.update()
        self.assertEqual(product.name, "Updated")

    def test_delete_product(self):
        product = ProductFactory()
        product.create()
        product_id = product.id
        product.delete()
        self.assertIsNone(Product.find(product_id))

    def test_list_all_products(self):
        ProductFactory.create_batch(3)
        self.assertEqual(len(Product.all()), 3)

    def test_find_by_name(self):
        ProductFactory(name="Soap").create()
        found = Product.find_by_name("Soap")
        self.assertGreater(len(found), 0)

    def test_find_by_category(self):
        ProductFactory(category="Hygiene").create()
        found = Product.find_by_category("Hygiene")
        self.assertGreater(len(found), 0)

    def test_find_by_availability(self):
        ProductFactory(available=True).create()
        found = Product.find_by_availability(True)
        self.assertGreater(len(found), 0)