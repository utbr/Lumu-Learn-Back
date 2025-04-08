from flask import jsonify, request

# Usuários simulados
Usuarios = [
    {
        'id': 1,
        'Usuario': 'Teste',
        'Senha': '123456'
    }
]

def configure_routes(app):
    @app.route('/login', methods=['GET'])
    def obter_usuarios():
        return jsonify(Usuarios)

    @app.route('/login', methods=['POST'])
    def verificar_login():
        dados = request.get_json()

        usuario_input = dados.get('Usuario')
        senha_input = dados.get('Senha')

        for usuario in Usuarios:
            if usuario['Usuario'] == usuario_input and usuario['Senha'] == senha_input:
                return jsonify({'mensagem': 'Login feito com sucesso', 'status': 'sucesso'}), 200

        return jsonify({'mensagem': 'Usuário ou senha incorretos', 'status': 'erro'}), 401
