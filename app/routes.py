from flask import jsonify, request

Usuarios = [
    {
        'id': 1,
        'Usuario': 'Teste',
        'Senha': '123456'
    }
]

def configure_routes(app):
    @app.route('/login', methods=['GET'])
    def obter_usuario():
        return jsonify(Usuarios)