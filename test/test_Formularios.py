#import model.package_model.Formulario as Formulario
from model.package_model.Formulario import Formulario
from datetime import datetime, date, time

obj_formulario = Formulario()
#lista_formularios = obj_formulario.obtener_formularios()

#-------------------LISTA DE FORMULARIOS-------------------
#if lista_formularios is not None:
#    for x in lista_formularios:
#        print(x)
#else:
#    print("No se encontraron datos de formularios")

#-------------------BUSQUEDA DE FORMULARIO POR ID-------------------
#print("\n=====================================\n")
#formulario_no_turno = obj_formulario.obtener_formulario_por_no_turno(1, 2)
#print(formulario_no_turno)

#-------------------BUSQUEDA DE FORMULARIO POR NOMBRE-------------------
#print("\n=====================================\n")
#nombre = 'Juan'
#paterno = 'Perez'
#materno = 'Lopez'
#formulario_nombre = obj_formulario.obtener_formulario_por_nombre(nombre, paterno, materno)
#print(formulario_nombre)

#-------------------BUSQUEDA DE FORMULARIO POR CURP-------------------
#print("\n=====================================\n")
#formulario_curp = obj_formulario.obtener_formulario_por_curp('ABCD123456HDFRRT01')
#print(formulario_curp)

#-------------------AGREGAR-------------------
#print("\n=================INSERTADO=================\n")
#no_turno = 0
#curp = 'AEAX010101MNEXXXR5'
#nombre = 'Jose'
#paterno = 'Pérez'
#materno = 'García'
#telefono = '5551234587'
#celular = '5559876583'
#correo = 'jose.perez@example.com'
#id_nivel = 1
#id_mun = 1
#id_asunto = 1
#estado = 'Pendiente'

#if len(curp) == 18:
#    obj_formulario_new = Formulario(no_turno, curp, nombre, paterno, materno, telefono, celular, correo, id_nivel, id_mun, id_asunto, estado)
#    result_ins = obj_formulario.agregar_formulario(obj_formulario_new)
#    if result_ins == 1:
#        print("Registro insertado correctamente")
#    else:
#        print("Error al insertar el registro")
#else:
#    print("Un dato es incorrecto, no se puede insertar")

#-------------------ELIMINAR-------------------
#print("\n=================BORRADO=================\n")
#no_turno = 2
#id_mun = 1
#result_del = obj_formulario.eliminar_formulario(no_turno, id_mun)
#if result_del == 1:
#    print("Registro eliminado correctamente")
#else:
#    print("Error al eliminar el registro")

#------------------ACTUALIZAR-------------------
#print("\n=================UPDATE=================\n")
#no_turno = 1
#curp = 'KXXX987654MNOPQRT0'
#nombre = 'Ximena'
#paterno = 'Kim'
#materno = 'X'
#telefono = '1112243334'
#celular = '4466556667'
#correo = 'kxx@example.com'
#id_nivel = 9
#id_mun = 1
#id_asunto = 3
#estado = 'Activo'

#if len(curp) == 18:
#    obj_formulario_new = Formulario(no_turno, curp, nombre, paterno, materno, telefono, celular, correo, id_nivel, id_mun, id_asunto, estado)
#    result_upd = obj_formulario.modificar_formulario(obj_formulario_new)
#    if result_upd == 1:
#        print("Registro actualizado correctamente")
#    else:
#        print("Error al actualizar el registro")
#else:
#    print("Un dato es incorrecto, no se puede actualizar")

#-------------------EXISTE-------------------
curp = 'ZYXW987654MNOPQRT0'
cuantos = Formulario.existe_formulario(curp)
print(cuantos)
