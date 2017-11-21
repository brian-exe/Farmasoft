from flask import Flask,render_template
from flask_login import LoginManager, login_user, login_required, logout_user,current_user
from ..classes.formularios import FormularioNuevaVenta
from ..classes.AdminDB import AdminDB
from flask import current_app as app
from ..classes.common import admin_needed

from . import consultas

@consultas.route('/lista',methods=['GET'])
@login_required
def listarCsv():
    admin = AdminDB(app.config['ARCHIVO_DB'])
    archivo = admin.dame_list_archivo()
    return render_template('lista.html',model=archivo)

@consultas.route('/AgregarVenta',methods=['GET'])
@login_required
@admin_needed
def agregarVGet():
    form = FormularioNuevaVenta()
    return render_template('agregarVenta.html',formulario=form,mostrar_mje=False)
    
@consultas.route('/AgregarVenta', methods=['POST'])
@login_required
@admin_needed
def agregarVPost():
    formulario=FormularioNuevaVenta()
    valida=formulario.validate_on_submit()
    if (valida):
        admin = AdminDB(app.config['ARCHIVO_DB'])
        admin.agregar_venta(formulario)
        formulario=FormularioNuevaVenta()
        return render_template('agregarVenta.html',formulario=formulario,mostrar_mje=True)
    return render_template('agregarVenta.html',formulario=formulario,mostrar_mje=False)


@consultas.route('/productosCliente/',methods=['GET'])
@consultas.route('/productosCliente',methods=['GET'])
@login_required
def prodXClienteG():
    admin=AdminDB(app.config['ARCHIVO_DB'])
    lista=admin.get_lista_clientes()
    return render_template('prodXCliente.html',lista_clientes=lista)

@consultas.route('/productosCliente/cliente=<cliente_name>',methods=['GET'])
@login_required
def prodXClienteP(cliente_name):
    admin=AdminDB(app.config['ARCHIVO_DB'])
    lista_productos=admin.get_productos_de_cliente(cliente_name)
    lista_clientes=admin.get_lista_clientes()
    return render_template('prodXCliente.html',lista_clientes=lista_clientes,lista_productos=lista_productos,busqueda=cliente_name)

@consultas.route('/clientesProductos/',methods=['GET'])
@consultas.route('/clientesProductos',methods=['GET'])
@login_required
def clienteXProdG():
    admin=AdminDB(app.config['ARCHIVO_DB'])
    lista=admin.get_lista_productos()
    return render_template('clientesXProd.html',lista_productos=lista)

@consultas.route('/clientesProductos/producto=<producto_name>',methods=['GET'])
@login_required
def clienteXProdP(producto_name):
    admin=AdminDB(app.config['ARCHIVO_DB'])
    lista_productos=admin.get_lista_productos()
    lista_clientes=admin.get_clientes_de_productos(producto_name)
    return render_template('clientesXProd.html',lista_clientes=lista_clientes,lista_productos=lista_productos,busqueda=producto_name)

@consultas.route('/masVendidos/',methods=['GET'])
@consultas.route('/masVendidos',methods=['GET'])
@login_required
def masVendidosG():
    return render_template('masVendidos.html')

@consultas.route('/masVendidos/cantResultados=<cant_resultados>',methods=['GET'])
@login_required
def masVendidosP(cant_resultados):
    admin=AdminDB(app.config['ARCHIVO_DB'])
    lista_resultados=admin.get_cant_mas_vendidos(cant_resultados)
    return render_template('masVendidos.html', lista_resultados=lista_resultados)
    
@consultas.route('/mejoresClientes/',methods=['GET'])
@consultas.route('/mejoresClientes',methods=['GET'])
@login_required
def mejoresClientesG():
    return render_template('mejoresClientes.html')
    
@consultas.route('/mejoresClientes/cantResultados=<cant_resultados>',methods=['GET'])
@login_required
def mejoresClientesP(cant_resultados):
    admin=AdminDB(app.config['ARCHIVO_DB'])
    lista_resultados=admin.get_cant_mejores_clientes(cant_resultados)
    return render_template('mejoresClientes.html', lista_resultados=lista_resultados)

