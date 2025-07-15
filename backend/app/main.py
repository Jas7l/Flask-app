from flask import Flask
from .database import Base, engine
from .routes.user import user_bp

Base.metadata.create_all(bind=engine)

app = Flask(__name__)

app.register_blueprint(user_bp)



