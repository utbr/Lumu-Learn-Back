from flask import Blueprint, request, jsonify
from .models import User
from . import db

main = Blueprint('main', __name__)


@main.route('/api/login', methods=['POST'])
def login():
    dados = request.json
    email = dados.get('email')
    senha = dados.get('senha')

    # Simulação de verificação futura no banco de dados
    if email == "usuario@teste.com" and senha == "123456":
        return jsonify({"status": "sucesso", "mensagem": "Login bem-sucedido"}), 200
    else:
        return jsonify({"status": "erro", "mensagem": "Credenciais inválidas"}), 401