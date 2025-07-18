from flask import Flask
from .extension import mail, login_manager
from .config import settings

from .database import Base, engine, SessionLocal
from .routes.user import user_bp
from .models.user import User

Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.config.update({
    "MAIL_SERVER": settings.MAIL_SERVER,
    "MAIL_PORT": settings.MAIL_PORT,
    "MAIL_USE_TLS": settings.MAIL_USE_TLS,
    "MAIL_USE_SSL": settings.MAIL_USE_SSL,
    "MAIL_USERNAME": settings.MAIL_USERNAME,
    "MAIL_PASSWORD": settings.MAIL_PASSWORD,
    "MAIL_DEFAULT_SENDER": settings.MAIL_DEFAULT_SENDER,
    "MAIL_SUPPRESS_SEND": settings.MAIL_SUPPRESS_SEND
})

login_manager.init_app(app)
mail.init_app(app)

app.secret_key = settings.SECRET_KEY


@login_manager.user_loader
def load_user(user_id):
    with SessionLocal() as db:
        user = db.query(User).filter(User.orbis_id == int(user_id)).first()
        return user


app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

