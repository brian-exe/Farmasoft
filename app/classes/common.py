'''Funciones comunes o compartidas por varios metodos'''
from flask_login import current_user
from functools import wraps
from flask import redirect,url_for
from flask import current_app as app
from .Config import Config

configurador=Config()

def admin_needed(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_admin():
            return f(*args, **kwargs)
        else:
            return redirect(url_for('auth.no_admin'))
    return decorated_function