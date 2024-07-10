#import model.package_model.Asunto as Asunto
from model.package_model.Asunto import Asunto 
from datetime import datetime,date,time

#obj_asunto = Asunto.Asunto()
#lista_asuntos = obj_asunto.obtener_asuntos()

#-------------------LISTA DE ASUNTOS------------------- 
#if lista_asuntos!=None:
#         for x in lista_asuntos:
#            print(x)
#else:
#    print("No se encontraron datos de asuntos")

#-------------------BUSQUEDA DE ASUNTOS-----------------     
#print("\n=====================================\n")
#asunto_id = obj_asunto.obtener_asunto_por_id(4)
#print(asunto_id)

#-------------------AGREGAR-------------------
#print("\n=================INSERTADO=================\n")
#id = 0
#nom = 'Vernos'
#if len(nom) > 2:
#    obj_asunto_new = Asunto.Asunto(id,nom)
#    result_ins = obj_asunto.agregar_asunto(obj_asunto_new)
#    if result_ins == 1:
#        print("Registro insertado correctamente")
#    else:
#        print("Error al insertar el registro")
#else:
#    print("Un dato es incorrecto, no se puede insertar")

#-------------------ELIMINAR-------------------  
#print("\n=================borrado=================\n")
#id = 7
#result_del = obj_asunto.eliminar_asunto(id)
#if result_del == 1:
#    print("Registro eliminado correctamente")
#else:
#    print("Error al eliminar el registro")
   
#------------------ACTUALIZAR-------------------
#print("\n=================update=================\n")
#id = 8
#nom = 'Veranos'
#if len(nom) > 2:
#     obj_asunto_new = Asunto.Asunto(id,nom)
#     result_upd = obj_asunto.modificar_asunto(obj_asunto_new)
#     if result_upd == 1:
#         print("Registro actualizado correctamente")
#     else:
#         print("Error al actualizar el registro")
#else:
#    print("Un dato es incorrecto, no se puede actualizar")

#-------------------EXISTE-------------------      
cuantos = Asunto.existe_asunto('Verano')
print(cuantos)
 