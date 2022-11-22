"""
    Initialize Flask Server
    """
from flask import Flask
from shop_app import db

def create_app():
    """Factory method that is automatically called by flask run,
    responsible for settings up routes and the database connection

    Returns:
        [Flask]: [A flask server]
    """
    # TODO, don't store secrets in code
    TEST_SECRET = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

    # create and configure the app
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=TEST_SECRET)
    app.url_map.strict_slashes = False

    db.init_app(app)

    # pylint: disable-next=C0415
    from . import profile, product, auth
    app.register_blueprint(auth.bp)
    app.register_blueprint(profile.bp)
    app.register_blueprint(product.bp)

    return app
