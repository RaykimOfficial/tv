import os
from flask import Flask, render_template, request, abort
from flask_login import LoginManager, current_user
from config import Config
from models import db, User, Channel
from auth import auth_bp, bcrypt as _bcrypt
from channels import channels_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Veritabanı ve bcrypt
    db.init_app(app)
    _bcrypt.init_app(app)

    # Login Manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"  # Blueprint uyumlu
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(channels_bp)

    # Ana Sayfa
    @app.route("/")
    def index():
        q = Channel.query.filter_by(is_public=True).order_by(Channel.created_at.desc())
        category = request.args.get("category")
        if category:
            q = q.filter(Channel.category == category)
        channels = q.all()
        return render_template("index.html", channels=channels)

    # Embed Player
    @app.route("/embed")
    def embed():
        channel_id = request.args.get("channel_id", type=int)
        if not channel_id:
            abort(400)
        ch = Channel.query.get_or_404(channel_id)
        return render_template("embed.html", channel=ch)

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    # Debug modu açık, hataları terminalde görebilirsin
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
