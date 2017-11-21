from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class FormularioNuevaVenta(FlaskForm):
    codigo= StringField("Codigo de Producto", validators=[DataRequired(message="Este campo es obligatorio")])
    producto= StringField("Nombre de Producto", validators=[DataRequired(message="Este campo es obligatorio")])
    cliente= StringField("Nombre Cliente", validators=[DataRequired(message="Este campo es obligatorio")])
    cantidad= StringField("Cantidad", validators=[DataRequired(message="Este campo es obligatorio")])
    precio= StringField("Precio del Producto", validators=[DataRequired(message="Este campo es obligatorio")])
    submit=SubmitField('Agregar')
    
    
class FormularioLogin(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message="Este campo es obligatorio")])
    password = PasswordField('Password',validators=[DataRequired(message="Este campo es obligatorio")])
    submit = SubmitField('Login')
    
class FormularioAlta(FlaskForm):
    username= StringField('Nombre de usuario',validators=[DataRequired(message="Este campo es obligatorio")])
    password = PasswordField('New Password', [DataRequired(message="Este campo es obligatorio"),EqualTo('confirm', message='Los passwords deben coincidir')])
    confirm = PasswordField('Repeat Password', [DataRequired(message="Este campo es obligatorio")])
    submit = SubmitField('Save')
    
class FormularioEditarUsuario(FlaskForm):
    username=StringField('Nombre de usuario',validators=[DataRequired(message="Este campo es obligatorio")])
    roles = SelectField(u'Rol de usuario',coerce=str)
    #role=StringField('Nombre de usuario',validators=[DataRequired(message="Este campo es obligatorio")])
    submit = SubmitField('Guardar')

class FormularioCambiarPassword(FlaskForm):
    actual_password= PasswordField('Contraseña actual',validators=[DataRequired(message="Este campo es obligatorio")])
    nueva_password = PasswordField('Nueva Password', [DataRequired(message="Este campo es obligatorio"),EqualTo('confirmar_password', message='Los passwords deben coincidir')])
    confirmar_password = PasswordField('Repita Password', [DataRequired(message="Este campo es obligatorio")])
    submit = SubmitField('Cambiar')