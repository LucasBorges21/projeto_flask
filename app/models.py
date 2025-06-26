from app import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String, nullable = False)
    empresa = db.Column(db.String, nullable = True)
    cidade = db.Column(db.String, nullable = True)
    estado = db.Column(db.String, nullable = True)
