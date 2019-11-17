from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/hello')
def hello():
    return "Hello from the other URL"