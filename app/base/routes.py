from flask import Flask,render_template,redirect,url_for
from flask_login import LoginManager, login_user, login_required, logout_user,current_user
from ..classes.validar import ValidationException
from ..classes.Config import Config
from ..classes.common import admin_needed
from . import base
from flask import current_app as app

configurador=Config()


def recargarConfiguraciones():
    if (configurador.reload_configurations()):
        app.config['ARCHIVO_DB']=configurador.get_path_to_data_file()
        app.config['ARCHIVO_USUARIOS']=configurador.get_path_to_users_file()

@base.route('/')
@base.route('/index')
def index():
    return render_template('index.html')

@base.route('/cambiarArchivo',methods=['GET'])
@login_required
@admin_needed
def cambiar_archivoG():
    model = {}
    model['lista_archivos']=configurador.get_lista_archivos()
    #Obtengo el nombre del archivo actual mediante spliteando el path completo sin el nombre del archivo
    model['archivo_actual']=configurador.ARCHIVO_DATOS.split(configurador.get_directory_data_file())[1]

    return render_template('cambiarArchivo.html',model=model)

@base.route('/cambiarArchivo/archivo=<archivo>',methods=['GET'])
@login_required
@admin_needed
def cambiar_archivoP(archivo):
    configurador.cambiar_archivo(archivo)
    recargarConfiguraciones()

    model = {}
    model['lista_archivos']=configurador.get_lista_archivos()
    #Obtengo el nombre del archivo actual mediante spliteando el path completo sin el nombre del archivo
    model['archivo_actual']=configurador.ARCHIVO_DATOS.split(configurador.get_directory_data_file())[1]

    return render_template('cambiarArchivo.html',model=model)