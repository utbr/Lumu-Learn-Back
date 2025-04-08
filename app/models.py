from . import db
import bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)

    def verificar_senha(self, senha):
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha_hash)

    @staticmethod
    def criar_usuario(email, senha):
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        return User(email=email, senha_hash=senha_hash)