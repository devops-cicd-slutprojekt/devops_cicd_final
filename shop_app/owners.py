from flask import Blueprint


bp = Blueprint('owners', __name__, url_prefix='/owners')

def GetOwners():
    return "Owners are: Erik and Forsman"

@bp.route("/")
def index():
    return GetOwners()
