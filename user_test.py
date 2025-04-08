from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    novo_usuario = User.criar_usuario("adm@gmail.com", "123456")
    db.session.add(novo_usuario)
    db.session.commit()
    print("Usuário criado com sucesso.")
