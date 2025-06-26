from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from app import db
from app.models import Cliente

class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    empresa = StringField('Empresa', validators=[DataRequired()])
    cidade = StringField('Cidade', validators=[DataRequired()])
    estado = StringField('Estado', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        cliente = Cliente (
            nome = self.nome.data,
            empresa = self.empresa.data,
            cidade = self.cidade.data,
            estado = self.estado.data,
        )

        db.session.add(cliente)
        db.session.commit()