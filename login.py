from flask_login import LoginManager
from db import db
from models import Usuario

lm = LoginManager()

@lm.user_loader
def user_loader(user_id):
    return db.session.query(Usuario).filter_by(id=user_id).first()