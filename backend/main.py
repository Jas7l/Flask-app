from flask import Flask
from flask_login import LoginManager
from .config import settings

from .database import Base, engine, SessionLocal
from .routes.user import user_bp
from .models.user import User

Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    with SessionLocal() as db:
        user = db.query(User).filter(User.orbis_id == int(user_id)).first()
        return user


app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

