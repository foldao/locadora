from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


unidades = db.Table('Unidades',
    db.Column('Filmes_id', db.Integer, db.ForeignKey('Filmes.id'), primary_key=True),
    db.Column('Usuario_id', db.Integer, db.ForeignKey('Usuarios.id'), primary_key=True)
)
class Usuarios(db.Model):
    __tablename__= 'Usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nome = db.Column(db.String(120), unique=False, nullable=False)

class Filmes(db.Model):
    __tablename__ = 'Filmes'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), unique=True, nullable=False)
    genero = db.Column(db.String(80), unique=False, nullable=True)
    ano_lancamento= db.Column(db.Integer, nullable=True)
    usuarios=db.relationship('Usuarios', secondary=unidades, lazy='subquery', backref=db.backref('filme', lazy=True))

if __name__ == "__main__":
    from app import create_app
    app=create_app()
    app.app_context().push()
    db.init_app(app)
    db.create_all()