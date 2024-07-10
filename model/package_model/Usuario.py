import model.package_model.Database as Database

class Usuarios:
    def __init__(self, no_usuario=0, usuario='', contrasena=''):
        self.__no_usuario = no_usuario
        self.__usuario = usuario
        self.__contrasena = contrasena
    
    def obtener_usuarios(self):
        conexion = Database.Database()
        usuarios = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT no_usuario, usuario, contrasena FROM usuarios")
            usuarios = cursor.fetchall()
        conexion.conn.close()
        return usuarios
    
    def obtener_usuario_por_no_usuario(self, no_usuario):
        conexion = Database.Database()
        usuario = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT no_usuario, usuario, contrasena FROM usuarios WHERE no_usuario = %s", (no_usuario))
            usuario = cursor.fetchone()
        conexion.conn.close()
        return usuario
    
    def agregar_usuario(self, obj_usu):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql = "INSERT INTO usuarios(usuario, contrasena) VALUES(%s, %s)"
                vals = (obj_usu.__usuario, obj_usu.__contrasena)
                affected = cursor.execute(sql, vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
    
    def eliminar_usuario(self, no_usuario):
        conexion = Database.Database()
        affected = 0
        with conexion.cursor as cursor:
            try:
                sql = "DELETE FROM usuarios WHERE no_usuario = %s"
                vals = (no_usuario)
                affected = cursor.execute(sql, vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
    
    def modificar_usuario(self, obj_usu):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql = "UPDATE usuarios SET usuario = %s, contrasena = %s WHERE no_usuario = %s"
                vals = (obj_usu.__usuario, obj_usu.__contrasena, obj_usu.__no_usuario)
                #print(f"Executing SQL: {sql} with values {vals}")  # Línea de depuración
                affected = cursor.execute(sql, vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                print(f"Exception: {e}") 
                return e
            finally:
                conexion.conn.close()
    
    @staticmethod
    def existe_usuario(usu):
        conexion = Database.Database()
        usuario = None
        with conexion.cursor as cursor:
            sql = "SELECT count(*) as ex FROM usuarios WHERE usuario = %s"
            vals = (usu)
            cursor.execute(sql, vals)
            usuario = cursor.fetchone()
        conexion.conn.close()
        return usuario[0]
