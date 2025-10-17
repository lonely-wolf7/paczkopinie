from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .database.dbFactory import create_db, seed_database

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    create_db(db, app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, Paczkomats, Reviews
    
    with app.app_context():
        db.create_all()
        seed_database(db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
