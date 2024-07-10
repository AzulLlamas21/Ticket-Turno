import model.package_model.Database as Database

class Nivel:
    def __init__(self, id_nivel=0, nombre_nivel=''):
        self.__id_nivel = id_nivel
        self.__nombre_nivel = nombre_nivel
    
    def obtener_niveles(self):
        conexion = Database.Database()
        niveles = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT id, nivel FROM nivel")
            niveles = cursor.fetchall()
        conexion.conn.close()
        return niveles
    
    def obtener_nivel_por_id(self, id):
        conexion = Database.Database()
        nivel = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT id, nivel FROM nivel WHERE id = %s", (id))
            nivel = cursor.fetchone()
        conexion.conn.close()
        return nivel
    
    def agregar_nivel(self, obj_nv):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql = "INSERT INTO nivel(nivel) VALUES(%s)"
                vals = (obj_nv.__nombre_nivel)
                affected = cursor.execute(sql, vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
    
    def eliminar_nivel(self, id):
        conexion = Database.Database()
        affected = 0
        with conexion.cursor as cursor:
            try:
                sql = "DELETE FROM nivel WHERE id = %s"
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
    
    def modificar_nivel(self, obj_nv):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql = "UPDATE nivel SET nivel = %s WHERE id = %s"
                vals = (obj_nv.__nombre_nivel, obj_nv.__id_nivel)
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
    def existe_nivel(nv):
        conexion = Database.Database()
        nivel = None
        with conexion.cursor as cursor:
            sql = "SELECT count(*) as ex FROM nivel WHERE nivel = %s"
            vals = (nv)
            cursor.execute(sql, vals)
            nivel = cursor.fetchone()
        conexion.conn.close()
        return nivel[0]
