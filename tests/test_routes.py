import json
from service.models import db
from service.routes import app
from tests.factories import ProductFactory

def test_read_product(client):
    product = ProductFactory()
    product.create()
    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200

def test_update_product(client):
    product = ProductFactory()
    product.create()
    data = product.serialize()
    data["name"] = "Updated"
    response = client.put(f"/products/{product.id}", json=data)
    assert response.status_code == 200
    assert response.get_json()["name"] == "Updated"

def test_delete_product(client):
    product = ProductFactory()
    product.create()
    response = client.delete(f"/products/{product.id}")
    assert response.status_code == 204

def test_list_all_products(client):
    ProductFactory.create_batch(3)
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.get_json()) >= 3

def test_search_by_name(client):
    ProductFactory(name="SpecialProduct").create()
    response = client.get("/products", query_string={"name": "SpecialProduct"})
    assert response.status_code == 200

def test_search_by_category(client):
    ProductFactory(category="Electronics").create()
    response = client.get("/products", query_string={"category": "Electronics"})
    assert response.status_code == 200

def test_search_by_availability(client):
    ProductFactory(available=True).create()
    response = client.get("/products", query_string={"available": "true"})
    assert response.status_code == 200