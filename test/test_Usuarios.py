#import model.package_model.Usuario as Usuarios
from model.package_model.Usuario import Usuarios
from datetime import datetime,date,time

#obj_usuario = Usuarios.Usuarios()
#lista_usuarios = obj_usuario.obtener_usuarios()

#-------------------LISTA DE ASUNTOS------------------- 
#if lista_usuarios!=None:
#         for x in lista_usuarios:
#            print(x)
#else:
#    print("No se encontraron datos de usuarios")

#-------------------BUSQUEDA DE ASUNTOS-----------------     
#print("\n=====================================\n")
#usuario_no_usuario = obj_usuario.obtener_usuario_por_no_usuario(4)
#print(usuario_no_usuario)

#-------------------AGREGAR-------------------
#print("\n=================INSERTADO=================\n")
#no_usuario = 0
#nom = 'roma'
#con = 'roma'
#if len(nom) > 2:
#    obj_usuario_new = Usuarios.Usuarios(no_usuario,nom,con)
#    result_ins = obj_usuario.agregar_usuario(obj_usuario_new)
#    if result_ins == 1:
#        print("Registro insertado correctamente")
#    else:
#        print("Error al insertar el registro")
#else:
#    print("Un dato es incorrecto, no se puede insertar")

#-------------------ELIMINAR-------------------  
#print("\n=================borrado=================\n")
#no_usuario = 4
#result_del = obj_usuario.eliminar_usuario(no_usuario)
#if result_del == 1:
#    print("Registro eliminado correctamente")
#else:
#    print("Error al eliminar el registro")
   
#------------------ACTUALIZAR-------------------
#print("\n=================update=================\n")
#no_usuario = 4
#nom = 'otro'
#con = 'otromas'
#if len(nom) > 2:
#    obj_usuario_new = Usuarios.Usuarios(no_usuario,nom,con)
#    result_upd = obj_usuario.modificar_usuario(obj_usuario_new)
#    if result_upd == 1:
#        print("Registro actualizado correctamente")
#    else:
#        print("Error al actualizar el registro")
#else:
#    print("Un dato es incorrecto, no se puede actualizar")

#-------------------EXISTE-------------------      
cuantos = Usuarios.existe_usuario('azul')
print(cuantos)

#-------------------VERIFICAR CREDENCIALES---------------
print("\n=================verificar=================\n")

usuario_correcto = 'a'
contrasena_correcta = 'azul'
#usuario_incorrecto = 'wrong_user'
#contrasena_incorrecta = 'wrong_password'

# Verificar usuario correcto
usuario = Usuarios.verificar_credenciales(usuario_correcto, contrasena_correcta)
if usuario:
    print("Test usuario correcto: PASSED")
else:
    print("Test usuario correcto: FAILED")

# Verificar usuario incorrecto
#usuario = Usuarios.verificar_credenciales(usuario_incorrecto, contrasena_incorrecta)
#if usuario:
#    print("Test usuario incorrecto: FAILED")
#else:
#    print("Test usuario incorrecto: PASSED")
