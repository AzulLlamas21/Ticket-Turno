import model.package_model.Database as Database

class Municipio:
    def __init__(self, id_municipio=0, nombre_municipio=''):
        self.__id_municipio=id_municipio
        self.__nombre_municipio=nombre_municipio
       
    def obtener_municipios(self):
        conexion = Database.Database()
        municipios = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT id,municipio FROM municipio")
            municipios = cursor.fetchall()
        conexion.conn.close()
        return municipios
   
    def obtener_municipio_por_id(self,id):
        conexion = conexion = Database.Database()
        municipio = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT id,municipio FROM municipio WHERE id = %s", (id))
            municipio = cursor.fetchone()
        conexion.conn.close()
        return municipio
   
    def agregar_municipio(self, obj_mun):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql="INSERT INTO municipio(municipio) VALUES(%s)"
                vals=(obj_mun.__nombre_municipio)
                affected=cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
               
    def eliminar_municipio(self, id):
        conexion = Database.Database()
        affected = 0
        with conexion.cursor as cursor:
            try:
                sql="DELETE FROM municipio WHERE id = %s"
                vals=(id)
                affected=cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
               
    def modificar_municipio(self, obj_mun):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql="UPDATE municipio SET municipio = %s WHERE id = %s"
                vals=(obj_mun.__nombre_municipio, obj_mun.__id_municipio)
                affected=cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
               
    @staticmethod
    def existe_municipio(mun):
        conexion = Database.Database()
        municipio = None
        with conexion.cursor as cursor:
            sql="SELECT count(*) as ex FROM municipio WHERE municipio = %s"
            vals=(mun)
            cursor.execute(sql, vals)
            municipio = cursor.fetchone()
        conexion.conn.close()
        return municipio[0]              
               
 