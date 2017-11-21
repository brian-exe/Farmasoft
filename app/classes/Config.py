import csv
import os

DIRECTORIO_ARCHIVOS='./archivos'
DIRECTORIO_DATOS=DIRECTORIO_ARCHIVOS+'/datos/'
ARCHIVO_CONFIG=DIRECTORIO_ARCHIVOS+'/config.conf'

class Config():
    def __init__(self):
        self.ARCHIVO_USUARIOS=""
        self.ARCHIVO_DATOS=""
        with open(ARCHIVO_CONFIG,'r') as f:
            reader=csv.reader(f,delimiter=':')
            for linea in reader:
                if linea[0]=='datos':
                    self.ARCHIVO_DATOS=linea[1]
                if linea[0]=='usuarios':
                    self.ARCHIVO_USUARIOS=linea[1]
                
    def get_path_to_users_file(self):
        return self.ARCHIVO_USUARIOS
    
    def get_path_to_data_file(self):
        return self.ARCHIVO_DATOS
        
    def reload_configurations(self):
        with open(ARCHIVO_CONFIG,'r') as f:
            reader=csv.reader(f,delimiter=':')
            for linea in reader:
                if linea[0]=='datos':
                    self.ARCHIVO_DATOS=linea[1]
                if linea[0]=='usuarios':
                    self.ARCHIVO_USUARIOS=linea[1]
        return True
    def get_directory_data_file(self):
        directory=DIRECTORIO_DATOS

        return directory

    def get_lista_archivos(self):
        directorio_datos= self.get_directory_data_file()
        lista=os.listdir(directorio_datos)
        return lista

    def cambiar_archivo(self,archivo_name):
        temp=ARCHIVO_CONFIG + '-temp'
        userfile=ARCHIVO_CONFIG
        
        with open(userfile, 'r') as csvFile:
            with open(temp, 'w') as tempfile:
                reader = csv.reader(csvFile, delimiter=':')
                for line in reader:
                    archivo=line[0]
                    path=line[1]
                    if (archivo=='datos'):
                        path=self.get_directory_data_file()+archivo_name
                    tempfile.write(archivo+':'+path+'\n')
        os.rename(temp, userfile)
