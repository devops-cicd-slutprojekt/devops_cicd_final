import os
import mysql.connector
from flask import g


def get_db_config():
    mysql_host = os.environ.get("MYSQL_HOST", default="127.0.0.1")
    mysql_user = os.environ.get("MYSQL_USER", default="username")
    mysql_database = os.environ.get("MYSQL_DATABASE", default="example")
    mysql_password = os.environ.get("MYSQL_PASSWORD")
    config = {
        "host": mysql_host,
        "user": mysql_user,
        "password": mysql_password,
        "database": mysql_database
    }
    return config


def get_db():
    """get_db will return a new database connection or reuse the existing one within the request context"""
    # pylint: disable=assigning-non-slot
    if 'database' not in g:
        g.database = mysql.connector.connect(**get_db_config())
        return g.database
    if not g.database.is_connected():
        g.database = mysql.connector.connect(**get_db_config())
        return g.database
    return g.database


# pylint: disable-next=unused-argument
def close_db(exception=None):
    """This function will close the database and remove it from the request context"""
    database = g.pop('database', None)
    if database is not None:
        database.close()


def init_app(app):
    """ init_app will register a tearing_down that closes the database after each request"""
    app.teardown_appcontext(close_db)
