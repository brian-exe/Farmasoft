from flask import Flask,render_template,redirect,url_for,request,flash
from ..classes.formularios import FormularioLogin,FormularioAlta,FormularioCambiarPassword,FormularioEditarUsuario
from flask import current_app as app
from ..classes.common import admin_needed
from ..classes.user_administration import User,UserRepository
from flask_login import LoginManager, login_user, login_required, logout_user,current_user

from . import auth

@auth.route('/alta',methods=['GET'])
def altaG():
    form = FormularioAlta()
            
    return render_template('alta.html',form=form,mostrar_mje=False)
    
@auth.route('/alta',methods=['POST'])
def altaP():
    user_admin =UserRepository(app.config['ARCHIVO_USUARIOS'])
    form = FormularioAlta()
    if (form.validate_on_submit()):
        if(form.password.data == form.confirm.data):
            if not(user_admin.check_user_exists(form.username.data)):                
                user_admin.add_user(form.username.data,form.password.data)
                return render_template('alta.html',form=form,mostrar_mje=True)
            else:
                flash('El usuario ya existe')
                return render_template('alta.html',form=form)
    return render_template('alta.html',form=form)

@auth.route('/login', methods=['GET'])
def loginG():
    if (current_user.is_authenticated):
        return redirect('/')
    else:
        form = FormularioLogin()
        return (render_template('login.html',form = form))
    
    
@auth.route('/login', methods=['POST'])
def loginP():
    form = FormularioLogin()
    if form.validate_on_submit():
        repository = UserRepository(app.config['ARCHIVO_USUARIOS'])
        user = repository.authenticate_user(form.name.data,form.password.data)
        if (user != None):
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('base.index'))
        else:
            flash('Usuario o contraseña inválida.')
            return render_template('login.html', form=form)

    return render_template('login.html', form=form,error=True)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('index.html')

@auth.route('/cambiarPassword',methods=['GET','POST'])
@login_required
def cambiar_password():
    form = FormularioCambiarPassword()
    if (form.validate_on_submit()):
        user_admin =UserRepository(app.config['ARCHIVO_USUARIOS'])
        if not(user_admin.validate_password(current_user.name,form.actual_password.data)):
            flash('La contraseña actual ingresada es incorrecta')
            form = FormularioCambiarPassword()
            return render_template('cambiarPassword.html',formulario=form)
        else:
            user_admin.change_password(current_user.name,form.nueva_password.data)
            flash('La contraseña se cambió correctamente.')
            form = FormularioCambiarPassword()
            return render_template('cambiarPassword.html',formulario=form)
    return render_template('cambiarPassword.html',formulario=form)

@auth.route('/editarRolesUsuarios',methods=['GET'])
@login_required
@admin_needed
def editar_usuarios():
    user_admin =UserRepository(app.config['ARCHIVO_USUARIOS'])
    model=user_admin.get_user_list()
    return render_template('editarUsuarios.html',model=model)
    
@auth.route('/editarRolUsuario/<usuario>',methods=['GET','POST'])
@login_required
@admin_needed
def editar_usuario(usuario):
    form=FormularioEditarUsuario()
    user_admin =UserRepository(app.config['ARCHIVO_USUARIOS'])
    user=user_admin.getUser(usuario)
    form.username.data=user.name
    form.roles.choices=user_admin.get_role_list()
    
    if form.validate_on_submit():
        user_admin.change_role_user(form.username.data,form.roles.data)
        return redirect(url_for('auth.editar_usuarios'))

    return render_template('editarUsuario.html',formulario=form)

@auth.route("/noAdmin")
def no_admin():
    return render_template('noAdmin.html')