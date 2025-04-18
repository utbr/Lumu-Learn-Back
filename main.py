from flask import Flask
from flask_cors import CORS  # importa o CORS
from db import db
from login import lm
from routes.routes_login import configure_routes

app = Flask(__name__)
app.secret_key = 'lancode'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

db.init_app(app)
lm.init_app(app)
lm.login_view = 'login'

configure_routes(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)