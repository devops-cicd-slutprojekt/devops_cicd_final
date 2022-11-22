import functools
from flask import (
    Blueprint, render_template, request, flash, redirect, url_for, session, g
)
from werkzeug.security import check_password_hash, generate_password_hash
from shop_app.db import get_db
from mysql.connector.errors import InterfaceError

bp = Blueprint('auth', __name__, url_prefix='/auth')


# pylint: disable=assigning-non-slot
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        with get_db().cursor(prepared=True) as cur:
            stmt = 'SELECT * FROM user WHERE id = %s'
            cur.execute(
                stmt, (user_id,)
            )
            g.user = cur.fetchone()


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                with db.cursor(prepared=True) as cur:
                    print((username, generate_password_hash(password)))
                    stmt = "INSERT INTO user (username, password) VALUES (%s, %s)"
                    cur.execute(
                        stmt, (username, generate_password_hash(password))
                    )
                    db.commit()
            except InterfaceError as e:
                print(e)
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@ bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        database = get_db()
        error = None
        with database.cursor(prepared=True) as cur:
            stmt = "SELECT * FROM user WHERE username = (%s)"
            cur.execute(
                stmt, (username, )
            )
            user = cur.fetchone()
            if user is None:
                error = 'Incorrect username.'
            elif not check_password_hash(user[2], password):
                error = 'Incorrect password.'

            if error is None:
                session.clear()
                session['user_id'] = user[0]
                return redirect(url_for('start.index'))

            flash(error)

    return render_template('auth/login.html')


@ bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('start.index'))


def login_required(view):
    @ functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
