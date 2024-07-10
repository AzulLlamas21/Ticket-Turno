#import model.package_model.Nivel as Nivel
from model.package_model.Nivel import Nivel
from datetime import datetime,date,time

#obj_niveles = Nivel.Nivel()
#lista_niveles = obj_niveles.obtener_niveles()
 
#-------------------LISTA DE NIVELES-------------------
#if lista_niveles!=None:
#    for x in lista_niveles:
#        print(x)
#else:
#    print("No se encontraron datos de niveles")
    
#-------------------BUSQUEDA DE NIVELES-------------------
#print("\n=====================================\n")
#niveles_id = obj_niveles.obtener_nivel_por_id(4)
#print(niveles_id)

#-------------------AGREGAR-------------------
#print("\n=============INSERTADO============\n")
#id = 0
#nom = '12'
#if len(nom) == 1 or len(nom) == 2:
#    obj_niveles_new = Nivel.Nivel(id,nom)
#    result_ins = obj_niveles.agregar_nivel(obj_niveles_new)
#    if result_ins == 1:
#        print("Registro insertado correctamente")
#    else:
#        print("Error al insertar el registro")
#else:
#    print("Un dato es incorrecto, no se puede insertar")

#-------------------ELIMINAR-------------------  
#print("\n=============borrado=============\n")
#id = 20
#result_del = obj_niveles.eliminar_nivel(id)
#if result_del == 1:
#    print("Registro eliminado correctamente")
#else:
#    print("Error al eliminar el registro")
 
#------------------ACTUALIZAR-------------------
#print("\=============update=============\n")
#id = 11
#nom = '11'
#if len(nom) == 1 or len(nom) == 2:
#    obj_niveles_new = Nivel.Nivel(id,nom)
#    result_upd = obj_niveles.modificar_nivel(obj_niveles_new)
#    if result_upd == 1:
#        print("Registro actualizado correctamente")
#    else:
#        print("Error al actualizar el registro")
#else:
#    print("Un dato es incorrecto, no se puede actualizar")
   
#-------------------EXISTE-------------------  
cuantos = Nivel.existe_nivel('12')
print(cuantos)
 