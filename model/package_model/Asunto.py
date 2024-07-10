import model.package_model.Database as Database

class Asunto:
    def __init__(self, id_asunto=0, nombre_asunto=''):
        self.__id_asunto = id_asunto
        self.__nombre_asunto = nombre_asunto
    
    def obtener_asuntos(self):
        conexion = Database.Database()
        asuntos = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT id, asunto FROM asunto")
            asuntos = cursor.fetchall()
        conexion.conn.close()
        return asuntos
    
    def obtener_asunto_por_id(self, id):
        conexion = Database.Database()
        asunto = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT id, asunto FROM asunto WHERE id = %s", (id))
            asunto = cursor.fetchone()
        conexion.conn.close()
        return asunto
    
    def agregar_asunto(self, obj_asto):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql = "INSERT INTO asunto(asunto) VALUES(%s)"
                vals = (obj_asto.__nombre_asunto)
                affected = cursor.execute(sql, vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
    
    def eliminar_asunto(self, id):
        conexion = Database.Database()
        affected = 0
        with conexion.cursor as cursor:
            try:
                sql = "DELETE FROM asunto WHERE id = %s"
                vals = (id)
                affected = cursor.execute(sql, vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
    
    def modificar_asunto(self, obj_asto):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql = "UPDATE asunto SET asunto = %s WHERE id = %s"
                vals = (obj_asto.__nombre_asunto, obj_asto.__id_asunto)
                affected = cursor.execute(sql, vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
    
    @staticmethod
    def existe_asunto(asto):
        conexion = Database.Database()
        asunto = None
        with conexion.cursor as cursor:
            sql = "SELECT count(*) as ex FROM asunto WHERE asunto = %s"
            vals = (asto)
            cursor.execute(sql, vals)
            asunto = cursor.fetchone()
        conexion.conn.close()
        return asunto[0]
