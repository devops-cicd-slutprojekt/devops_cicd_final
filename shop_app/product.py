from flask import (
    Blueprint, jsonify, request
)
from shop_app.db import get_db

bp = Blueprint('product', __name__, url_prefix='/product')


def include_column_names(resultset, description):
    column_names = [row[0] for row in description]
    return [dict(zip(column_names, row)) for row in resultset]


@bp.route("/")
def index():
    """Show all the products"""
    with get_db().cursor() as cur:
        cur.execute(
            "SELECT * from products"
            " ORDER BY name DESC"
        )
        products = cur.fetchall()
        return jsonify(include_column_names(products, cur.description))


@bp.route("/", methods=('POST',))
def create_product():
    """Add a product"""
    json_payload = request.get_json()
    if json_payload:
        database = get_db()
        with database.cursor(prepared=True) as cur:
            stmt = "INSERT INTO products(name, price) VALUES (%s, %s)"
            cur.execute(
                stmt, (json_payload['name'], int(json_payload['price']))
            )
            database.commit()
            return jsonify({"status": "ok"})
    return jsonify({"error": "Failed to parse json"}), 400
