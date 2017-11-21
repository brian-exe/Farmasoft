from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from .classes.Config import Config
from .classes.validar import ValidationException
from flask_login import LoginManager
from .classes.user_administration import User,UserRepository


def create_app():
    #Configuracions basicas del objeto app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '$$hard$$secret$$key$$'
    boot = Bootstrap(app)
    ###

    # Inicializacion Flask-Login
    login_manager = LoginManager()
    login_manager.setup_app(app)
    login_manager.login_view = "auth.loginG"

    @login_manager.user_loader
    def load_user(user_id):
        return UserRepository(app.config['ARCHIVO_USUARIOS']).getUser(user_id)
    ####

    # Configuraciones usadas por los metodos que leen los archivos
    configurador = Config()
    app.config['ARCHIVO_DB']=configurador.get_path_to_data_file()
    app.config['ARCHIVO_USUARIOS']=configurador.get_path_to_users_file()
    ###

    # Configuracion de los BluePrints
    from .auth import auth as auth
    app.register_blueprint(auth)

    from .base import base as base
    app.register_blueprint(base)

    from .consultas import consultas as consultas
    app.register_blueprint(consultas)
    ###

    ##Manejo de errores####################

    #Error handler personalizado para atrapar las excepciones de validacion que pudieran ocurrir#
    @app.errorhandler(ValidationException)
    def custom_handler(e):
        return render_template('customError.html', mensaje=e.message )
        
    @app.errorhandler(401)
    def not_authorized(e):
        return redirect(url_for('auth.loginG'))

    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def error_interno(e):
        return render_template('500.html'), 500    

    ##Fin Manejo de errores#################

    return app
