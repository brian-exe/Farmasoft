import csv

class ValidationException(Exception):
    def __init__(self,message=''):
        self.message=message
    def __repr__(self):
        print(message)

class Validador():
    def __init__(self, path=''):
        self.filePath=path
        self.cabecera={}
        self.cabecera['icodigo']=-1
        self.cabecera['icliente']=-1
        self.cabecera['iproducto']=-1
        self.cabecera['icantidad']=-1
        self.cabecera['iprecio']=-1
        
    def validar_archivo(self):
        if (self.filePath == ''):
            raise ValidationException('Error, la ruta al archivo no está configurada')
        else:
            numLinea=0
            try:
                with open(self.filePath,'r') as f:
                    reader= csv.reader(f)
                    for linea in reader:
                        if(numLinea == 0):
                            self.setCabecera(linea)
                            numLinea+=1
                        else:
                            self.comprobarCantidadCampos(linea,numLinea)
                            
                            cliente=linea[self.cabecera['icliente']]
                            codigo=linea[self.cabecera['icodigo']]
                            producto=linea[self.cabecera['iproducto']]
                            cantidad=linea[self.cabecera['icantidad']]
                            precio=linea[self.cabecera['iprecio']]
                            
                            self.comprobarCampoVacio(codigo,numLinea)
                            self.comprobarEntero(cantidad,numLinea)
                            self.comprobarDecimal(precio,numLinea)
                            numLinea+=1
            except ValueError:
                raise ValidationException('Error, el archivo no existe, o no se puede abrir.')
        return True
                        
    def setCabecera(self,listaCabecera):
        cantCabecera=0
        for i in range(len(listaCabecera)):
            if listaCabecera[i]=='CLIENTE':
                self.cabecera['icliente']=i
                cantCabecera+=1
            if listaCabecera[i] =='CODIGO':
                self.cabecera['icodigo']=i
                cantCabecera+=1
            if listaCabecera[i] =='PRODUCTO':
                self.cabecera['iproducto']=i
                cantCabecera+=1
            if listaCabecera[i] =='CANTIDAD':
                self.cabecera['icantidad']=i
                cantCabecera+=1
            if listaCabecera[i] =='PRECIO':
                self.cabecera['iprecio']=i
                cantCabecera+=1
        if (cantCabecera !=5):
                raise ValidationException('Error, la cabecera es incorrecta')
                 
    def comprobarCantidadCampos(self,linea,numLinea):
        if (len(linea) != 5):
            raise ValidationException("Error en Linea nro "+str(numLinea)+" del archivo. Cantidad invalida de campos.")
            
    def comprobarCampoVacio(self,campo,numLinea):
        if(campo ==''):
            raise ValidationException("Error en Linea nro "+str(numLinea)+" del  archivo. Campo vacío.")
            
    def comprobarEntero(self,campo,numLinea):
        try:
            aux=int(campo)
        except ValueError:
            raise ValidationException("Error en Linea nro "+str(numLinea)+" tipo no admitido en campo cantidad.")
            
    def comprobarDecimal(self,campo,numLinea):
        try:
            aux=float(campo)
        except ValueError:
            raise ValidationException("Error en Linea nro "+str(numLinea)+" tipo no admitido en campo precio.")
