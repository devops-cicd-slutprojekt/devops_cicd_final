from flask import (
    Blueprint, jsonify
)
from shop_app.db import get_db

bp = Blueprint('testerproduct', __name__, url_prefix='/testerproduct')


def include_column_names(resultset, description):
    column_names = [row[0] for row in description]
    return [dict(zip(column_names, row)) for row in resultset]

def get_search_pattern():
    return "test%"

@bp.route("/")
def index():
    """Show all the products"""
    with get_db().cursor() as cur:
        cur.execute(
            "SELECT * from products"
            " WHERE name LIKE %s", [get_search_pattern()]
        )
        products = cur.fetchall()
        return jsonify(include_column_names(products, cur.description))
