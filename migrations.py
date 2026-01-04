from flask_migrate import Migrate
from website import create_app, db

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        # Importowanie modeli, aby migracje mogły je wykryć
        from website.models import User, Reviews, Paczkomats, City
        
        # Tworzenie wszystkich tabel w bazie danych
        db.create_all()