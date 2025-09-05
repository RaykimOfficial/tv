from getpass import getpass
from app import create_app
from models import db, User
from flask_bcrypt import Bcrypt

app = create_app()
bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()
    username = input("Admin kullanıcı adı: ").strip()
    password = input("Şifre: ")
    if User.query.filter_by(username=username).first():
        print("Bu kullanıcı adı zaten var.")
    else:
        u = User(username=username, password_hash=bcrypt.generate_password_hash(password).decode("utf-8"), is_admin=True)
        db.session.add(u)
        db.session.commit()
        print("Admin kullanıcı oluşturuldu.")
