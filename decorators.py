from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not getattr(current_user, "is_admin", False):
            flash("Bu sayfa için admin girişi gerekli.", "danger")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper
