from app import create_app, db
from models import User  # User modelini kendi projenize göre import et

app = create_app()

def delete_user():
    username = input("Silmek istediğiniz kullanıcı adı: ")
    with app.app_context():  # 🔑 burada context açıyoruz
        user = User.query.filter_by(username=username).first()
        if user:
            confirm = input(f"{username} gerçekten silinsin mi? (E/h): ").lower()
            if confirm == 'e':
                db.session.delete(user)
                db.session.commit()
                print(f"Kullanıcı '{username}' silindi.")
            else:
                print("İşlem iptal edildi.")
        else:
            print(f"Kullanıcı '{username}' bulunamadı.")

if __name__ == "__main__":
    delete_user()
