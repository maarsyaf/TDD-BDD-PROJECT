# service/models.py

class Product:
    _products = []
    _id_counter = 1

    def __init__(self, name="", category="", available=True, price=0.0):
        self.id = Product._id_counter
        Product._id_counter += 1

        self.name = name
        self.category = category
        self.available = available
        self.price = price

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "available": self.available,
            "price": self.price,
        }

    def deserialize(self, data):
        self.name = data.get("name", "")
        self.category = data.get("category", "")
        self.available = data.get("available", True)
        self.price = data.get("price", 0.0)

    def create(self):
        Product._products.append(self)
        return self

    def update(self, data):
        self.deserialize(data)
        return self

    def delete(self):
        Product._products = [p for p in Product._products if p.id != self.id]

    @classmethod
    def find(cls, product_id):
        for product in cls._products:
            if product.id == product_id:
                return product
        return None

    @classmethod
    def all(cls):
        return cls._products

    @classmethod
    def find_by_name(cls, name):
        return [p for p in cls._products if name.lower() in p.name.lower()]

    @classmethod
    def find_by_category(cls, category):
        return [p for p in cls._products if category.lower() in p.category.lower()]

    @classmethod
    def find_by_availability(cls, available):
        return [p for p in cls._products if p.available == available]
