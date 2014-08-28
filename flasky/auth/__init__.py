from flask import Blueprint

auth = Blueprint('auth', __name__)

# import views into auth module namespace for convenience
from . import views


# define decorators for view permissions
from ..models import Permission
from functools import wraps
from flask import abort
from flask.ext.login import current_user

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
