from flask import (
    Blueprint, jsonify
)
from shop_app.db import get_db

bp = Blueprint('testerproduct', __name__, url_prefix='/testerproduct')


def include_column_names(resultset, description):
    column_names = [row[0] for row in description]
    return [dict(zip(column_names, row)) for row in resultset]


@bp.route("/")
def index():
    """Show all the products"""
    with get_db().cursor() as cur:
        cur.execute(
            "SELECT * from products"
            " WHERE name LIKE 'test%'"
        )
        products = cur.fetchall()
        return jsonify(include_column_names(products, cur.description))
