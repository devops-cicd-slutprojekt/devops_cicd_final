from flask import Blueprint, render_template

bp = Blueprint('start', __name__, url_prefix='/')


@bp.route("/")
def index():
    return render_template('profile.html')
