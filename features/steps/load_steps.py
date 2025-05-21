from behave import given
from service.models import db, Product

@given('the following products')
def step_impl(context):
    db.drop_all()
    db.create_all()
    for row in context.table:
        product = Product(
            name=row['name'],
            category=row['category'],
            available=row['available'].lower() == "true",
            price=float(row['price'])
        )
        product.create()