from flask import Flask
from flask_login import LoginManager
import sqlalchemy

from .database import Base, engine, SessionLocal
from .routes.user import user_bp
from .models.user import User

Base.metadata.create_all(bind=engine)

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    with SessionLocal() as db:
        user = db.query(User).filter(User.orbis_id == int(user_id)).first()
        return user

app.register_blueprint(user_bp)



