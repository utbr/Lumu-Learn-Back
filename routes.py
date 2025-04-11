from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from models import Usuario
from db import db
from flask import jsonify
from flask_cors import CORS
import hashlib

def hash(txt):
    return hashlib.sha256(txt.encode('utf-8')).hexdigest()

def configure_routes(app):
    @app.route('/')
    @login_required
    def home():
        print(current_user)
        return render_template('home.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            nome = request.form['nomeForm']
            senha = request.form['senhaForm']
            user = db.session.query(Usuario).filter_by(nome=nome, senha=hash(senha)).first()
            if not user:
                return 'Nome ou senha incorreto'
            login_user(user)
            return redirect(url_for('home'))

# Novo endpoint de login para React
    @app.route('/api/login', methods=['POST'])
    def api_login():
        data = request.get_json()
        nome = data.get('nome')
        senha = data.get('senha')
        
        user = db.session.query(Usuario).filter_by(nome=nome, senha=hash(senha)).first()
        if not user:
            return jsonify({'success': False, 'message': 'Nome ou senha incorretos'}), 401
        
        login_user(user)
        return jsonify({'success': True, 'message': 'Login bem-sucedido'})



    @app.route('/registrar', methods=['GET', 'POST'])
    def registrar():
        if request.method == 'GET':
            return render_template('registrar.html')
        elif request.method == 'POST':
            nome = request.form['nomeForm']
            senha = request.form['senhaForm']
            novo_usuario = Usuario(nome=nome, senha=hash(senha))
            db.session.add(novo_usuario)
            db.session.commit()
            login_user(novo_usuario)
            return redirect(url_for('home'))

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))
