import csv
import os

class User():
    def __init__(self, name, password,role):
        self.name = name
        self.password = password
        self.role=role

    def __repr__(self):
        return '<User %r>' % self.name
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.name)
        
    def is_admin(self):
        return self.has_role('admin')
        
    def has_role(self, role):
        return self.role==role
        
    

class UserRepository():
    def __init__(self,path=''):
        self.filePath=path

    def add_user(self,username,password):
        archivo = open(self.filePath,'a')
        try:
            linea= str(username)+','+ str(password)+',user'+'\n'
            archivo.write(linea)
        finally:
            archivo.close()
            
    def get_role_list(self):
        #Se puede reemplazar por leer desde un archivo los roles, pero no me pareció que valga la pena
        return [('user','Usuario'),('admin','Administrador')]

    def authenticate_user(self,name,password):
        with open(self.filePath,'r') as usersFile:
            user = None
            for line in usersFile:
                line_list= line.split(",")
                str_user=line_list[0].strip()
                str_pass=line_list[1].strip()
                str_role=line_list[2].strip()

                if (name == str_user):
                    if (password== str_pass):
                        user=User(name,password,str_role)
        return user
        
    def getUser(self,name):
        with open(self.filePath,'r') as usersFile:
            user = None
            for line in usersFile:
                line_list= line.split(",")
                str_user=line_list[0].strip()
                str_pass=line_list[1].strip()
                str_role=line_list[2].strip()
                
                if (name == str_user):
                    user=User(str_user,str_pass,str_role)
        return user
    
    def get_user_list(self):
        result=[]
        result.append(['Nombre de usuario','Rol asignado'])
        with open(self.filePath,'r') as f:
            reader=csv.reader(f)
            for line in reader:
                list_line=[]
                list_line.append(line[0])
                list_line.append(line[2])
                result.append(list_line)
        return result
        
    '''Metodo creado para poder cambiar el rol de los usuarios'''
    def change_role_user(self,user,new_role):
        temp=self.filePath + '-temp'
        userfile=self.filePath
        
        with open(userfile, 'r') as csvFile:
            with open(temp, 'w') as tempfile:
                reader = csv.reader(csvFile, delimiter=',')
                for line in reader:
                    username=line[0]
                    password=line[1]
                    role=line[2]
                    if (username==user):
                        role=new_role
                    tempfile.write(username+','+password+','+role+'\n')
        os.rename(temp, userfile)
    
    def check_user_exists(self,username):
        found=False
        with open(self.filePath,'r') as f:
            reader= csv.reader(f)
            for line in reader:
                if (line[0]==username):
                    found=True
        return found
    
    def validate_password(self, username,password):
        is_ok=False
        with open(self.filePath,'r') as f:
            reader= csv.reader(f)
            for line in reader:
                if (line[0] == username):
                    if(line[1] == password):
                        is_ok=True
        return is_ok
    
    def change_password(self,username,new_password):
        temp=self.filePath + '-temp'
        userfile=self.filePath
        
        with open(userfile, 'r') as csvFile:
            with open(temp, 'w') as tempfile:
                reader = csv.reader(csvFile, delimiter=',')
                for line in reader:
                    user=line[0]
                    password=line[1]
                    role=line[2]
                    if (user==username):
                        password=new_password
                    tempfile.write(user+','+password+','+role+'\n')
        os.rename(temp, userfile)