from db import db
from flask_login import UserMixin
from datetime import datetime


class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True, nullable=False)
    senha = db.Column(db.String, nullable=False)

    exercicios = db.relationship("Exercicio", back_populates="usuario", cascade="all, delete-orphan")


class Exercicio(db.Model):
    __tablename__ = "exercicios"

    id = db.Column(db.Integer, primary_key=True)
    codigo_lista = db.Column(db.String(36), nullable=False)  # UUID como string para agrupar exercícios
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    area = db.Column(db.String(50), nullable=False)        # Ex: Matemática, História
    assunto = db.Column(db.String(100), nullable=False)    # Ex: Função Afim
    dificuldade = db.Column(db.String(20), nullable=False) # Ex: Fácil, Médio, Difícil
    corpo = db.Column(db.Text, nullable=False)

    alternativa_a = db.Column(db.String(255), nullable=False)
    alternativa_b = db.Column(db.String(255), nullable=False)
    alternativa_c = db.Column(db.String(255), nullable=False)
    resposta_correta = db.Column(db.String(1), nullable=False)  # 'A', 'B' ou 'C'

    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    usuario = db.relationship("Usuario", back_populates="exercicios")
