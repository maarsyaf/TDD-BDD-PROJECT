from factory import Factory, Faker
from service.models import Product

class ProductFactory(Factory):
    class Meta:
        model = Product

    name = Faker("word")
    category = Faker("word")
    available = Faker("boolean")
    price = Faker("pyfloat", left_digits=3, right_digits=2, positive=True)