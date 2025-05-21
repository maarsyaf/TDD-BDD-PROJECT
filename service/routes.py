from flask import Flask,Blueprint, request, jsonify, abort
from service.models import Product

bp = Blueprint("products", __name__, url_prefix="/products")

@bp.route("", methods=["GET"])
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name:
        results = Product.find_by_name(name)
    elif category:
        results = Product.find_by_category(category)
    elif available is not None:
        results = Product.find_by_availability(available.lower() == "true")
    else:
        results = Product.all()

    return jsonify([p.serialize() for p in results]), 200

@bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404)
    return jsonify(product.serialize()), 200

@bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404)
    data = request.get_json()
    product.deserialize(data)
    product.update()
    return jsonify(product.serialize()), 200

@bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404)
    product.delete()
    return "", 204