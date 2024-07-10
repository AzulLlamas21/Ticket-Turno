#import model.package_model.Municipio as Municipio
from model.package_model.Municipio import Municipio
from datetime import datetime,date,time

#obj_municipio = Municipio.Municipio()
#lista_municipios = obj_municipio.obtener_municipios()
 
#-------------------LISTA DE MUNICIPIOS-------------------
#if lista_municipios!=None:
#    for x in lista_municipios:
#        print(x)
#else:
#    print("No se encontraron datos de municipios")
    
#-------------------BUSQUEDA DE MUNICIPIO-------------------
#print("\n=====================================\n")
#municipio_id = obj_municipio.obtener_municipio_por_id(4)
#print(municipio_id)

#-------------------AGREGAR-------------------
#print("\n=============INSERTADO============\n")
#id = 0
#nom = 'Alaboso'
#if len(nom) > 2:
#    obj_municipio_new = Municipio.Municipio(id,nom)
#    result_ins = obj_municipio.agregar_municipio(obj_municipio_new)
#    if result_ins == 1:
#        print("Registro insertado correctamente")
#    else:
#        print("Error al insertar el registro")
#else:
#    print("Un dato es incorrecto, no se puede insertar")

#-------------------ELIMINAR-------------------  
#print("\n=============borrado=============\n")
#id = 9
#result_del = obj_municipio.eliminar_municipio(id)
#if result_del == 1:
#    print("Registro eliminado correctamente")
#else:
#    print("Error al eliminar el registro")
 
#------------------ACTUALIZAR-------------------
#print("\=============update=============\n")
#id = 11
#nom = 'San Buenaventura'
#if len(nom) > 2:
#    obj_municipio_new = Municipio.Municipio(id,nom)
#    result_upd = obj_municipio.modificar_municipio(obj_municipio_new)
#    if result_upd == 1:
#        print("Registro actualizado correctamente")
#    else:
#        print("Error al actualizar el registro")
#else:
#    print("Un dato es incorrecto, no se puede actualizar")
   
#-------------------EXISTE-------------------  
cuantos = Municipio.existe_municipio('San Buenaventura')
print(cuantos)
 