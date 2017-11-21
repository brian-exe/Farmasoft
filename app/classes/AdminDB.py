from .validar import *
import csv
import operator

class AdminDB():
    def __init__(self,ruta=''):
        self.ruta_archivo=ruta
        validador=Validador(self.ruta_archivo)
        validador.validar_archivo()
        self.set_indices(validador.cabecera)
    
    def set_indices(self,dicc_cabecera):
        self.indices=dicc_cabecera
    
    def dame_list_archivo(self):
        with open(self.ruta_archivo, 'r') as f:
            reader = csv.reader(f)
            lista = list(reader)
        return lista
        
    def agregar_venta(self,form):
        linea=''
        linea +=str(form.codigo.data)+','
        linea +=str(form.producto.data)+','
        linea +=str(form.cliente.data)+','
        linea +=str(form.cantidad.data)+','
        linea +=str(form.precio.data)+'\n'
        with open(self.ruta_archivo, 'a') as f:
            f.write(linea)
                  
    def get_lista_clientes(self):
        with open(self.ruta_archivo, 'r') as f:
            reader = csv.reader(f)
            lista_clientes=[]
            indice=self.indices['icliente']
            for linea in reader:
                lista_clientes.append(linea[indice])
            return list(set(lista_clientes))
            
    def get_productos_de_cliente(self,cliente_name):
        with open(self.ruta_archivo, 'r') as f:
            reader = csv.reader(f)
            lista_productos=[]
            indiceC=self.indices['icliente']
            titulos=['Codigo Producto', 'Descripcion','Cantidad','Precio']
            lista_productos.append(titulos)
            for linea in reader:
                if (linea[indiceC]==cliente_name):
                    codigo=linea[self.indices['icodigo']]
                    producto=linea[self.indices['iproducto']]
                    cantidad=linea[self.indices['icantidad']]
                    precio=linea[self.indices['iprecio']]
                    lista=[codigo,producto,cantidad,precio]
                    lista_productos.append(lista)
                    
            return lista_productos

    def get_lista_productos(self):
        with open(self.ruta_archivo, 'r') as f:
            reader = csv.reader(f)
            lista_productos=[]
            indice=self.indices['iproducto']
            linea = next(reader)#Para quitar los titulos de los resultados
            for linea in reader:
                lista_productos.append(linea[indice])
            return list(set(lista_productos))
            
    def get_clientes_de_productos(self,producto_name):
        with open(self.ruta_archivo, 'r') as f:
            reader = csv.reader(f)
            lista_clientes=[]
            indiceP=self.indices['iproducto']
            titulos=['Cliente','Cantidad','Precio']
            lista_clientes.append(titulos)
            for linea in reader:
                if (linea[indiceP]==producto_name):
                    cliente=linea[self.indices['icliente']]
                    cantidad=linea[self.indices['icantidad']]
                    precio=linea[self.indices['iprecio']]
                    lista=[cliente,cantidad,precio]
                    lista_clientes.append(lista)
                    
            return lista_clientes
    #Metodo que retorna todos los productos ordenados por cantidad de ventas
    def get_mas_vendidos(self):
        with open(self.ruta_archivo,'r') as f:
            reader=csv.reader(f)
            dict_resultados={}
            primer_linea=next(reader)#Desapilo la primer linea#
            for linea in reader:
                producto=linea[self.indices['iproducto']]
                cantidad=int(linea[self.indices['icantidad']])
                if (producto in dict_resultados):
                    cant_actual=int(dict_resultados[producto])
                    dict_resultados[producto]=cant_actual+cantidad
                else:
                    dict_resultados[producto]=cantidad
        return sorted(dict_resultados.items(), key=operator.itemgetter(1),reverse=True)
        
    #Metodo que retorna la cantidad de resultados deseados a partir de todos los mas vendidos
    def get_cant_mas_vendidos(self,cant_resultados):
        total=self.get_mas_vendidos()
        resultado=[]
        resultado.append(['Producto','Cantidad'])
        iteraciones=min(int(cant_resultados),len(total))
        for i in range(int(iteraciones)):
            resultado.append(total[i])
        return resultado
        
    #Metodo que retorna todos los clientes ordenados por compras (precio)
    def get_mejores_clientes(self):
        with open(self.ruta_archivo,'r') as f:
            reader=csv.reader(f)
            dict_resultados={}
            primer_linea=next(reader)#Desapilo la primer linea#
            for linea in reader:
                cliente=linea[self.indices['icliente']]
                precio=float(linea[self.indices['iprecio']])
                if (cliente in dict_resultados):
                    precio_actual=float(dict_resultados[cliente])
                    dict_resultados[cliente]=precio_actual+precio
                else:
                    dict_resultados[cliente]=precio
        return sorted(dict_resultados.items(), key=operator.itemgetter(1),reverse=True)
        
    #Metodo que retorna la cantidad de resultados deseados a partir de los mejores clientes
    def get_cant_mejores_clientes(self,cant_resultados):
        total=self.get_mejores_clientes()
        resultado=[]
        resultado.append(['Cliente','Precio'])
        iteraciones=min(int(cant_resultados),len(total))
        for i in range(int(iteraciones)):
            resultado.append(total[i])
        return resultado
