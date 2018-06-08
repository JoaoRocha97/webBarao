from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    nome = db.Column(db.String(60), index=True)
    sobrenome = db.Column(db.String(60), index=True)
    senha_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def senha(self):
        raise AttributeError('senha não pode ser vista.')

    @senha.setter
    def senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verify_senha(self, senha):
        return check_password_hash(self.password_hash, senha)

    def __repr__(self):
        return '<Usuario: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(id_usuario):
    return Usuario.query.get(int(id_usuario))
